import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RunSurvey = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    selectedSurvey: '',
    subjects: [
      {
        subject: '',
        respondants: [],
        categoryWeights: {}
      }
    ]
  });

  // Sample data - in real app, this would come from API
  const surveys = [
    'Leadership Skills Assessment',
    'Communication Skills Survey',
    'Team Management Review',
    'Project Management Skills'
  ];

  const subjects = [
    'John Doe',
    'Jane Smith',
    'Robert Brown',
    'Lisa Anderson'
  ];

  const respondants = [
    { name: 'Sarah Wilson', category: 'Peer' },
    { name: 'Mike Johnson', category: 'Subordinate' },
    { name: 'Emily Davis', category: 'Boss' },
    { name: 'David Wilson', category: 'Customer' },
    { name: 'Tom Harris', category: 'Peer' },
    { name: 'Lisa Anderson', category: 'Super Boss' },
    { name: 'Robert Brown', category: 'Subordinate' }
  ];

  const handleSurveyChange = (e) => {
    setFormData(prev => ({
      ...prev,
      selectedSurvey: e.target.value
    }));
  };

  const handleSubjectChange = (index, value) => {
    setFormData(prev => ({
      ...prev,
      subjects: prev.subjects.map((item, i) => 
        i === index ? { ...item, subject: value, respondants: [], categoryWeights: {} } : item
      )
    }));
  };

  const handleRespondantChange = (subjectIndex, respondantName) => {
    setFormData(prev => ({
      ...prev,
      subjects: prev.subjects.map((item, i) => 
        i === subjectIndex 
          ? {
              ...item,
              respondants: item.respondants.includes(respondantName)
                ? item.respondants.filter(r => r !== respondantName)
                : [...item.respondants, respondantName]
            }
          : item
      )
    }));
  };

  const handleCategoryWeightChange = (subjectIndex, category, weight) => {
    setFormData(prev => ({
      ...prev,
      subjects: prev.subjects.map((item, i) => 
        i === subjectIndex 
          ? {
              ...item,
              categoryWeights: {
                ...item.categoryWeights,
                [category]: weight
              }
            }
          : item
      )
    }));
  };

  const addSubject = () => {
    setFormData(prev => ({
      ...prev,
      subjects: [...prev.subjects, { subject: '', respondants: [], categoryWeights: {} }]
    }));
  };

  const removeSubject = (index) => {
    if (formData.subjects.length > 1) {
      setFormData(prev => ({
        ...prev,
        subjects: prev.subjects.filter((_, i) => i !== index)
      }));
    }
  };

  const getAvailableSubjects = (currentIndex) => {
    const selectedSubjects = formData.subjects
      .map((item, index) => index !== currentIndex ? item.subject : null)
      .filter(Boolean);
    return subjects.filter(subject => !selectedSubjects.includes(subject));
  };

  const handleStart = (e) => {
    e.preventDefault();
    
    // Validation
    if (!formData.selectedSurvey) {
      alert('Please select a survey');
      return;
    }
    
    const validSubjects = formData.subjects.filter(item => item.subject && item.respondants.length > 0);
    if (validSubjects.length === 0) {
      alert('Please select at least one subject with respondants');
      return;
    }

    console.log('Survey execution data:', { ...formData, subjects: validSubjects });
    alert('Survey started successfully!');
    navigate('/');
  };

  const handleCancel = () => {
    navigate('/');
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <button 
          onClick={handleCancel}
          style={{
            background: 'none',
            border: 'none',
            color: '#d946ef',
            fontSize: '0.875rem',
            cursor: 'pointer',
            marginBottom: '1rem',
            display: 'flex',
            alignItems: 'center'
          }}
        >
          ← Back to Dashboard
        </button>
        <h1 className="page-title">Run Survey</h1>
        <p className="page-description">
          Configure and start a new survey execution with selected participants.
        </p>
      </div>

      {/* Run Survey Form */}
      <div className="card">
        <form onSubmit={handleStart} style={{ padding: '2rem' }}>
          {/* Select Survey */}
          <div style={{ marginBottom: '2rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Select Survey *
            </label>
            <select
              value={formData.selectedSurvey}
              onChange={handleSurveyChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
            >
              <option value="">Choose a survey</option>
              {surveys.map((survey) => (
                <option key={survey} value={survey}>{survey}</option>
              ))}
            </select>
          </div>

          {/* Dynamic Subjects Section */}
          <div style={{ marginBottom: '2rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <h3 style={{ fontSize: '1rem', fontWeight: '600', color: '#374151' }}>
                Subjects and Respondants
              </h3>
              <button
                type="button"
                onClick={addSubject}
                className="btn-secondary"
                style={{ fontSize: '0.75rem', padding: '0.5rem 1rem' }}
              >
                + Add Subject
              </button>
            </div>

            {formData.subjects.map((subjectItem, index) => (
              <div key={index} style={{ 
                border: '1px solid #e5e7eb', 
                borderRadius: '0.5rem', 
                padding: '1.5rem', 
                marginBottom: '1rem',
                backgroundColor: index % 2 === 0 ? '#fafafa' : '#f0f9ff'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                  <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#374151' }}>
                    Subject {index + 1}
                  </h4>
                  {formData.subjects.length > 1 && (
                    <button
                      type="button"
                      onClick={() => removeSubject(index)}
                      style={{
                        background: 'none',
                        border: 'none',
                        color: '#dc2626',
                        cursor: 'pointer',
                        fontSize: '0.875rem'
                      }}
                    >
                      Remove
                    </button>
                  )}
                </div>

                {/* Subject Selection */}
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                    Select Subject *
                  </label>
                  <select
                    value={subjectItem.subject}
                    onChange={(e) => handleSubjectChange(index, e.target.value)}
                    required
                    style={{
                      width: '100%',
                      padding: '0.75rem',
                      border: '1px solid #d1d5db',
                      borderRadius: '0.375rem',
                      fontSize: '0.875rem'
                    }}
                  >
                    <option value="">Choose a subject</option>
                    {getAvailableSubjects(index).map((subject) => (
                      <option key={subject} value={subject}>{subject}</option>
                    ))}
                  </select>
                </div>

                {/* Respondants Selection */}
                {subjectItem.subject && (
                  <div>
                    <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                      Select Respondants for {subjectItem.subject} * (Multiple selection)
                    </label>
                    <div style={{
                      border: '1px solid #d1d5db',
                      borderRadius: '0.375rem',
                      padding: '0.75rem',
                      maxHeight: '200px',
                      overflow: 'auto',
                      backgroundColor: 'white'
                    }}>
                      {respondants.map((respondant) => (
                        <label key={respondant.name} style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          marginBottom: '0.5rem',
                          cursor: 'pointer',
                          padding: '0.5rem',
                          border: '1px solid #e5e7eb',
                          borderRadius: '0.25rem',
                          backgroundColor: subjectItem.respondants.includes(respondant.name) ? '#f0f9ff' : 'white'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center' }}>
                            <input
                              type="checkbox"
                              checked={subjectItem.respondants.includes(respondant.name)}
                              onChange={() => handleRespondantChange(index, respondant.name)}
                              style={{ marginRight: '0.5rem' }}
                            />
                            <div>
                              <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{respondant.name}</span>
                              <span style={{ 
                                fontSize: '0.75rem', 
                                color: '#6b7280',
                                marginLeft: '0.5rem',
                                backgroundColor: '#f3f4f6',
                                padding: '0.125rem 0.5rem',
                                borderRadius: '0.75rem'
                              }}>
                                {respondant.category}
                              </span>
                            </div>
                          </div>
                        </label>
                      ))}
                    </div>
                    {subjectItem.respondants.length > 0 && (
                      <p style={{ fontSize: '0.75rem', color: '#6b7280', marginTop: '0.5rem' }}>
                        Selected: {subjectItem.respondants.join(', ')}
                      </p>
                    )}

                    {/* Category Weights Section */}
                    {subjectItem.respondants.length > 0 && (
                      <div style={{ marginTop: '1.5rem' }}>
                        <h5 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                          Category Weightages
                        </h5>
                        {(() => {
                          const selectedCategories = [...new Set(
                            respondants
                              .filter(r => subjectItem.respondants.includes(r.name))
                              .map(r => r.category)
                          )];
                          
                          return selectedCategories.map((category) => (
                            <div key={category} style={{ 
                              display: 'flex', 
                              alignItems: 'center', 
                              justifyContent: 'space-between',
                              marginBottom: '0.75rem',
                              padding: '0.5rem',
                              backgroundColor: '#f9fafb',
                              borderRadius: '0.25rem'
                            }}>
                              <label style={{ fontSize: '0.875rem', fontWeight: '500', color: '#374151' }}>
                                {category}
                              </label>
                              <input
                                type="number"
                                min="0"
                                max="100"
                                step="1"
                                value={subjectItem.categoryWeights[category] || ''}
                                onChange={(e) => handleCategoryWeightChange(index, category, e.target.value)}
                                placeholder="Weight %"
                                style={{
                                  width: '80px',
                                  padding: '0.375rem',
                                  border: '1px solid #d1d5db',
                                  borderRadius: '0.25rem',
                                  fontSize: '0.75rem',
                                  textAlign: 'center'
                                }}
                              />
                            </div>
                          ));
                        })()}
                        <p style={{ fontSize: '0.75rem', color: '#6b7280', fontStyle: 'italic' }}>
                          Note: Assign percentage weights to each category. Total should ideally sum to 100%.
                        </p>
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end', marginTop: '2rem' }}>
            <button
              type="button"
              onClick={handleCancel}
              className="btn-secondary"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
            >
              Start Survey
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default RunSurvey;
