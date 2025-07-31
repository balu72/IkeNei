import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { surveysAPI } from '../../services/api';

const DomainSurveys = () => {
  const navigate = useNavigate();
  const [surveysData, setSurveysData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch surveys data from API
  useEffect(() => {
    const fetchSurveys = async () => {
      try {
        setLoading(true);
        const response = await surveysAPI.getMySurveys();
        if (response.success) {
          setSurveysData(response.data || []);
        } else {
          setError('Failed to fetch surveys');
        }
      } catch (err) {
        setError(err.message || 'Failed to fetch surveys');
      } finally {
        setLoading(false);
      }
    };

    fetchSurveys();
  }, []);

  const handleCreateSurvey = () => {
    console.log('Create New Survey clicked');
    navigate('/create-survey');
  };

  const handleBack = () => {
    navigate('/');
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
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
          ← Back to Dashboard
        </button>
        <h1 className="page-title">Survey Management</h1>
        <p className="page-description">
          Create, manage, and monitor surveys for your domain. Track survey performance and analyze feedback data.
        </p>
      </div>

      {/* Create Survey Button */}
      <div style={{ marginBottom: '2rem', display: 'flex', justifyContent: 'flex-end' }}>
        <button 
          className="btn-primary" 
          onClick={handleCreateSurvey}
          style={{ 
            padding: '0.75rem 1.5rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Survey
        </button>
      </div>

      {/* Survey Overview Table */}
      <div>
        <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
          Survey Overview
        </h2>
        
        <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
          <table style={{ 
            width: '100%', 
            borderCollapse: 'collapse',
            fontSize: '0.875rem'
          }}>
            <thead>
              <tr style={{ backgroundColor: '#f9fafb', borderBottom: '1px solid #e5e7eb' }}>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Survey Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Traits
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Weightage
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Status
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Report
                </th>
              </tr>
            </thead>
            <tbody>
              {surveysData.length > 0 ? (
                surveysData.map((survey) => (
                  <tr key={survey.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                      {survey.name || survey.surveyName}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                      {survey.traits ? survey.traits.map(trait => trait.name).join(', ') : 'No traits assigned'}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                      {survey.traits ? survey.traits.map(trait => `${trait.weight}%`).join(', ') : 'N/A'}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={{
                        backgroundColor: survey.status === 'active' ? '#dcfce7' : survey.status === 'draft' ? '#fef3c7' : '#fee2e2',
                        color: survey.status === 'active' ? '#166534' : survey.status === 'draft' ? '#d97706' : '#dc2626',
                        padding: '0.25rem 0.75rem',
                        borderRadius: '1rem',
                        fontSize: '0.75rem',
                        fontWeight: '500'
                      }}>
                        {survey.status === 'active' ? 'Active' : survey.status === 'draft' ? 'Draft' : 'Completed'}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      {survey.status === 'completed' ? (
                        <a 
                          href="#" 
                          style={{
                            color: '#3b82f6',
                            textDecoration: 'underline',
                            fontSize: '0.875rem',
                            fontWeight: '500'
                          }}
                          onClick={(e) => {
                            e.preventDefault();
                            console.log('View report for survey:', survey.id);
                          }}
                        >
                          View Report
                        </a>
                      ) : (
                        <span style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                          Not Available
                        </span>
                      )}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" style={{ 
                    padding: '2rem', 
                    textAlign: 'center', 
                    color: '#6b7280',
                    fontStyle: 'italic'
                  }}>
                    {loading ? 'Loading surveys...' : 'No surveys found. Create your first survey to get started.'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Summary Stats */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1rem',
        marginTop: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#10b981', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'draft').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'completed').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Completed Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {surveysData.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Surveys</p>
        </div>
      </div>
    </div>
  );
};

export default DomainSurveys;
