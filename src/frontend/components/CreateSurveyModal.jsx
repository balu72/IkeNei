import { useState } from 'react';

const CreateSurveyModal = ({ isOpen, onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    surveyName: '',
    competencies: []
  });

  const competenciesList = [
    'Leadership',
    'Communication',
    'Problem Solving',
    'Team Management',
    'Strategic Thinking',
    'Decision Making',
    'Adaptability',
    'Innovation',
    'Customer Focus',
    'Technical Skills'
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleCompetencyChange = (competency) => {
    setFormData(prev => ({
      ...prev,
      competencies: prev.competencies.includes(competency)
        ? prev.competencies.filter(c => c !== competency)
        : [...prev.competencies, competency]
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({
      surveyName: '',
      competencies: []
    });
  };

  const handleClose = () => {
    setFormData({
      surveyName: '',
      competencies: []
    });
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000
    }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '0.5rem',
        padding: '2rem',
        width: '90%',
        maxWidth: '600px',
        maxHeight: '90vh',
        overflow: 'auto'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: '600', color: '#374151' }}>
            Create New Survey
          </h2>
          <button
            onClick={handleClose}
            style={{
              background: 'none',
              border: 'none',
              fontSize: '1.5rem',
              cursor: 'pointer',
              color: '#6b7280'
            }}
          >
            ×
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Survey Name *
            </label>
            <input
              type="text"
              name="surveyName"
              value={formData.surveyName}
              onChange={handleInputChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
              placeholder="Enter survey name"
            />
          </div>

          <div style={{ marginBottom: '1rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Competencies (Select multiple)
            </label>
            <div style={{
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              padding: '0.75rem',
              maxHeight: '200px',
              overflow: 'auto'
            }}>
              {competenciesList.map((competency) => (
                <label key={competency} style={{
                  display: 'flex',
                  alignItems: 'center',
                  marginBottom: '0.5rem',
                  cursor: 'pointer'
                }}>
                  <input
                    type="checkbox"
                    checked={formData.competencies.includes(competency)}
                    onChange={() => handleCompetencyChange(competency)}
                    style={{ marginRight: '0.5rem' }}
                  />
                  <span style={{ fontSize: '0.875rem' }}>{competency}</span>
                </label>
              ))}
            </div>
            {formData.competencies.length > 0 && (
              <p style={{ fontSize: '0.75rem', color: '#6b7280', marginTop: '0.5rem' }}>
                Selected: {formData.competencies.join(', ')}
              </p>
            )}
          </div>

          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end', marginTop: '1.5rem' }}>
            <button
              type="button"
              onClick={handleClose}
              className="btn-secondary"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateSurveyModal;
