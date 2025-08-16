import { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { surveysAPI } from '../../services/api';

const SurveyDetails = () => {
  const navigate = useNavigate();
  const { surveyId } = useParams();
  const { isSystemAdmin } = useAuth();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [surveyData, setSurveyData] = useState(null);

  // Redirect if not system admin
  useEffect(() => {
    if (!isSystemAdmin) {
      navigate('/');
      return;
    }
  }, [isSystemAdmin, navigate]);

  // Fetch survey data
  useEffect(() => {
    const fetchSurvey = async () => {
      if (!surveyId) {
        setError('Invalid survey ID');
        setLoading(false);
        return;
      }

      try {
        setLoading(true);
        const response = await surveysAPI.getById(surveyId);
        
        if (response.success && response.data) {
          setSurveyData(response.data);
        } else {
          setError('Failed to fetch survey details');
        }
      } catch (error) {
        console.error('Error fetching survey:', error);
        setError('Error fetching survey: ' + error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSurvey();
  }, [surveyId]);

  const handleBack = () => {
    navigate('/analytics');
  };

  const getStateStyle = (status) => {
    const styles = {
      'draft': { backgroundColor: '#f3f4f6', color: '#374151' },
      'active': { backgroundColor: '#dcfce7', color: '#166534' },
      'inactive': { backgroundColor: '#fef3c7', color: '#d97706' },
      'completed': { backgroundColor: '#dbeafe', color: '#1e40af' },
      'archived': { backgroundColor: '#f3e8ff', color: '#7c3aed' }
    };
    
    return {
      ...styles[status] || styles['draft'],
      padding: '0.5rem 1rem',
      borderRadius: '1rem',
      fontSize: '0.875rem',
      fontWeight: '500',
      display: 'inline-block'
    };
  };

  const getStatusDisplayName = (status) => {
    const names = {
      'draft': 'Draft',
      'active': 'Active',
      'inactive': 'Inactive',
      'completed': 'Completed',
      'archived': 'Archived'
    };
    return names[status] || status;
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'Not specified';
    try {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    } catch (error) {
      return 'Invalid date';
    }
  };

  if (loading) {
    return (
      <div style={{ maxWidth: '1000px', margin: '0 auto', padding: '2rem', textAlign: 'center' }}>
        <div style={{
          width: '3rem',
          height: '3rem',
          border: '3px solid #d946ef',
          borderTop: '3px solid transparent',
          borderRadius: '50%',
          animation: 'spin 1s linear infinite',
          margin: '0 auto 1rem'
        }}></div>
        <p style={{ color: '#6b7280' }}>Loading survey details...</p>
      </div>
    );
  }

  if (error || !surveyData) {
    return (
      <div style={{ maxWidth: '1000px', margin: '0 auto', padding: '2rem' }}>
        <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
          <p style={{ color: '#dc2626', fontSize: '1.125rem', marginBottom: '1rem' }}>
            {error || 'Survey not found'}
          </p>
          <button onClick={handleBack} className="btn-secondary">
            Back to Survey Management
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <button 
          onClick={handleBack}
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
          ← Back to Survey Management
        </button>
        <h1 className="page-title">Survey Details</h1>
        <p className="page-description">
          Detailed information about the selected survey.
        </p>
      </div>

      {/* Survey Information */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div style={{ padding: '2rem' }}>
          {/* Basic Information */}
          <div style={{ marginBottom: '2rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
              <h2 style={{ fontSize: '1.5rem', fontWeight: '600', color: '#374151', margin: 0 }}>
                {surveyData.title}
              </h2>
              <span style={getStateStyle(surveyData.status)}>
                {getStatusDisplayName(surveyData.status)}
              </span>
            </div>
            
            {surveyData.description && (
              <p style={{ color: '#6b7280', fontSize: '1rem', lineHeight: '1.6', marginBottom: '1.5rem' }}>
                {surveyData.description}
              </p>
            )}
          </div>

          {/* Survey Details Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', marginBottom: '2rem' }}>
            <div>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                Survey Information
              </h3>
              <div style={{ space: '1rem' }}>
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Survey ID
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.id}
                  </p>
                </div>
                
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Account/Organization
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.account_name || surveyData.sector || surveyData.domain || surveyData.organization || 'Not specified'}
                  </p>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Created Date
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {formatDate(surveyData.created_at)}
                  </p>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Last Updated
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {formatDate(surveyData.updated_at)}
                  </p>
                </div>
              </div>
            </div>

            <div>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                Survey Configuration
              </h3>
              <div style={{ space: '1rem' }}>
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Survey Type
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.survey_type || '360-Degree Feedback'}
                  </p>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Total Questions
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.questions?.length || surveyData.total_questions || 'Not specified'}
                  </p>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Estimated Duration
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.estimated_duration || 'Not specified'}
                  </p>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.25rem' }}>
                    Response Count
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0 }}>
                    {surveyData.response_count || 0} responses
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Traits/Competencies Section */}
          {surveyData.traits && surveyData.traits.length > 0 && (
            <div style={{ marginBottom: '2rem' }}>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                Traits/Competencies ({surveyData.traits.length})
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '1rem' }}>
                {surveyData.traits.map((trait, index) => (
                  <div key={index} style={{
                    padding: '1rem',
                    backgroundColor: '#f9fafb',
                    border: '1px solid #e5e7eb',
                    borderRadius: '0.5rem'
                  }}>
                    <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#374151', marginBottom: '0.5rem' }}>
                      {trait.name || trait.title || `Trait ${index + 1}`}
                    </h4>
                    {trait.description && (
                      <p style={{ fontSize: '0.75rem', color: '#6b7280', margin: 0, lineHeight: '1.4' }}>
                        {trait.description}
                      </p>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Questions Section */}
          {surveyData.questions && surveyData.questions.length > 0 && (
            <div style={{ marginBottom: '2rem' }}>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                Survey Questions ({surveyData.questions.length})
              </h3>
              <div style={{ space: '1rem' }}>
                {surveyData.questions.slice(0, 5).map((question, index) => (
                  <div key={index} style={{
                    padding: '1rem',
                    backgroundColor: '#f9fafb',
                    border: '1px solid #e5e7eb',
                    borderRadius: '0.5rem',
                    marginBottom: '1rem'
                  }}>
                    <p style={{ fontSize: '0.875rem', color: '#374151', margin: 0, fontWeight: '500' }}>
                      {index + 1}. {question.text || question.question || question}
                    </p>
                    {question.type && (
                      <p style={{ fontSize: '0.75rem', color: '#6b7280', margin: '0.5rem 0 0 0' }}>
                        Type: {question.type}
                      </p>
                    )}
                  </div>
                ))}
                {surveyData.questions.length > 5 && (
                  <p style={{ fontSize: '0.875rem', color: '#6b7280', fontStyle: 'italic', textAlign: 'center' }}>
                    ... and {surveyData.questions.length - 5} more questions
                  </p>
                )}
              </div>
            </div>
          )}

          {/* Additional Information */}
          {(surveyData.instructions || surveyData.notes) && (
            <div>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#374151', marginBottom: '1rem' }}>
                Additional Information
              </h3>
              {surveyData.instructions && (
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.5rem' }}>
                    Instructions
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', lineHeight: '1.6', margin: 0 }}>
                    {surveyData.instructions}
                  </p>
                </div>
              )}
              {surveyData.notes && (
                <div>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#6b7280', marginBottom: '0.5rem' }}>
                    Notes
                  </label>
                  <p style={{ fontSize: '0.875rem', color: '#374151', lineHeight: '1.6', margin: 0 }}>
                    {surveyData.notes}
                  </p>
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      {/* Action Buttons */}
      <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end', marginBottom: '2rem' }}>
        <button
          onClick={handleBack}
          className="btn-secondary"
        >
          Back to Survey Management
        </button>
      </div>
    </div>
  );
};

export default SurveyDetails;
