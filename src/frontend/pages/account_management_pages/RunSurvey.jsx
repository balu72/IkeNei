import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { surveysAPI, subjectsAPI, respondentsAPI } from '../../services/api';

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

  // API data state
  const [surveys, setSurveys] = useState([]);
  const [subjects, setSubjects] = useState([]);
  const [respondents, setRespondents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch data from APIs
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Fetch active surveys, user's subjects, and user's respondents
        const [surveysRes, subjectsRes, respondentsRes] = await Promise.all([
          surveysAPI.getAvailable(), // Should return only active surveys
          subjectsAPI.getAll(),      // Filtered by current user's account
          respondentsAPI.getAll()    // Filtered by current user's account
        ]);
        
        if (surveysRes.success) {
          setSurveys(surveysRes.data || []);
        }
        if (subjectsRes.success) {
          setSubjects(subjectsRes.data || []);
        }
        if (respondentsRes.success) {
          setRespondents(respondentsRes.data || []);
        }
        
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err.message || 'Failed to load data');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

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

  const handleRespondantChange = (subjectIndex, respondantId) => {
    setFormData(prev => ({
      ...prev,
      subjects: prev.subjects.map((item, i) => 
        i === subjectIndex 
          ? {
              ...item,
              respondants: item.respondants.includes(respondantId)
                ? item.respondants.filter(r => r !== respondantId)
                : [...item.respondants, respondantId]
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
    const selectedSubjectIds = formData.subjects
      .map((item, index) => index !== currentIndex ? item.subject : null)
      .filter(Boolean);
    return subjects.filter(subject => !selectedSubjectIds.includes(subject.id));
  };

  const handleStart = async (e) => {
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

    try {
      // Transform data for API
      const transformedData = {
        survey_id: formData.selectedSurvey,
        subjects: validSubjects.map(subjectItem => ({
          subject_id: subjectItem.subject,
          respondent_ids: subjectItem.respondants,
          category_weights: subjectItem.categoryWeights
        }))
      };

      console.log('Survey execution data:', transformedData);
      
      // Call API to run survey
      const response = await surveysAPI.runSurvey(formData.selectedSurvey, transformedData);
      
      if (response.success) {
        alert('Survey started successfully!');
        navigate('/');
      } else {
        alert('Failed to start survey: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (err) {
      console.error('Error starting survey:', err);
      alert('Failed to start survey: ' + err.message);
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  // Loading state
  if (loading) {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Run Survey</h1>
        <div style={{ padding: '2rem' }}>
          <p>Loading surveys, subjects, and respondents...</p>
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Run Survey</h1>
        <div style={{ padding: '2rem', color: '#dc2626' }}>
          <p>Error: {error}</p>
          <button 
            onClick={() => window.location.reload()}
            className="btn-primary"
            style={{ marginTop: '1rem' }}
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

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
                <option key={survey.id || survey._id} value={survey.id || survey._id}>
                  {survey.title || survey.name}
                </option>
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
                      <option key={subject.id || subject._id} value={subject.id || subject._id}>
                        {subject.name}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Respondants Selection */}
                {subjectItem.subject && (
                  <div>
                    <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                      Select Respondants for {subjects.find(s => (s.id || s._id) === subjectItem.subject)?.name || 'Selected Subject'} * (Multiple selection)
                    </label>
                    <div style={{
                      border: '1px solid #d1d5db',
                      borderRadius: '0.375rem',
                      padding: '0.75rem',
                      maxHeight: '200px',
                      overflow: 'auto',
                      backgroundColor: 'white'
                    }}>
                      {respondents.map((respondent) => (
                        <label key={respondent.id || respondent._id} style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          marginBottom: '0.5rem',
                          cursor: 'pointer',
                          padding: '0.5rem',
                          border: '1px solid #e5e7eb',
                          borderRadius: '0.25rem',
                          backgroundColor: subjectItem.respondants.includes(respondent.id || respondent._id) ? '#f0f9ff' : 'white'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center' }}>
                            <input
                              type="checkbox"
                              checked={subjectItem.respondants.includes(respondent.id || respondent._id)}
                              onChange={() => handleRespondantChange(index, respondent.id || respondent._id)}
                              style={{ marginRight: '0.5rem' }}
                            />
                            <div>
                              <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{respondent.name}</span>
                              <span style={{ 
                                fontSize: '0.75rem', 
                                color: '#6b7280',
                                marginLeft: '0.5rem',
                                backgroundColor: '#f3f4f6',
                                padding: '0.125rem 0.5rem',
                                borderRadius: '0.75rem'
                              }}>
                                {respondent.relationship || respondent.category}
                              </span>
                            </div>
                          </div>
                        </label>
                      ))}
                    </div>
                    {subjectItem.respondants.length > 0 && (
                      <p style={{ fontSize: '0.75rem', color: '#6b7280', marginTop: '0.5rem' }}>
                        Selected: {subjectItem.respondants.map(id => 
                          respondents.find(r => (r.id || r._id) === id)?.name || id
                        ).join(', ')}
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
                            respondents
                              .filter(r => subjectItem.respondants.includes(r.id || r._id))
                              .map(r => r.relationship || r.category)
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
