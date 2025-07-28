import { useNavigate } from 'react-router-dom';

const DomainSurveys = () => {
  const navigate = useNavigate();

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
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>Leadership Skills Assessment</td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  Strategic Thinking<br/>
                  Decision Making<br/>
                  Team Management
                </td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  40%<br/>
                  35%<br/>
                  25%
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Active
                  </span>
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
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
                      console.log('View report for Leadership Skills Assessment');
                    }}
                  >
                    View Report
                  </a>
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>Communication Skills Survey</td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  Verbal Communication<br/>
                  Written Communication<br/>
                  Active Listening<br/>
                  Presentation Skills
                </td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  30%<br/>
                  25%<br/>
                  25%<br/>
                  20%
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Active
                  </span>
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
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
                      console.log('View report for Communication Skills Survey');
                    }}
                  >
                    View Report
                  </a>
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>Team Management Review</td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  Delegation<br/>
                  Conflict Resolution<br/>
                  Performance Management
                </td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  45%<br/>
                  30%<br/>
                  25%
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                  <span style={{
                    backgroundColor: '#fef3c7',
                    color: '#d97706',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Submitted For Approval
                  </span>
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                  <span style={{ color: '#6b7280', fontSize: '0.875rem' }}>
                    Not Available
                  </span>
                </td>
              </tr>
              <tr>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>Project Management Skills</td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  Planning & Organization<br/>
                  Risk Management<br/>
                  Resource Allocation<br/>
                  Timeline Management
                </td>
                <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                  35%<br/>
                  25%<br/>
                  20%<br/>
                  20%
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                  <span style={{
                    backgroundColor: '#fee2e2',
                    color: '#dc2626',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Completed
                  </span>
                </td>
                <td style={{ padding: '1rem', verticalAlign: 'top' }}>
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
                      console.log('View report for Project Management Skills');
                    }}
                  >
                    View Report
                  </a>
                </td>
              </tr>
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
            2
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            1
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>
            1
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Completed Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            4
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Surveys</p>
        </div>
      </div>
    </div>
  );
};

export default DomainSurveys;
