import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

const DomainAdminHome = () => {
  const navigate = useNavigate();
  const [showModal, setShowModal] = useState(null);

  const handleCreateSurvey = () => {
    console.log('Create New Survey clicked');
    // Navigate to survey creation page or show modal
    navigate('/create-survey');
  };

  const handleAddTrait = () => {
    console.log('Add New Trait clicked');
    // Navigate to trait creation page
    navigate('/create-trait');
  };

  const handleOpenAccount = () => {
    console.log('Open New Account clicked');
    // Navigate to account creation page
    navigate('/create-account');
  };

  const handleDefineReport = () => {
    console.log('Define New Report clicked');
    // Navigate to report definition page or show modal
    navigate('/reports');
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">Domain Admin Dashboard</h1>
        <p className="page-description">
          Create and manage surveys/questionnaires, oversee domain users, and analyze feedback data.
        </p>
      </div>

      {/* Quick Stats */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#10b981',
            marginBottom: '0.5rem'
          }}>
            15
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Surveys
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Feedback collection active
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#d946ef',
            marginBottom: '0.5rem'
          }}>
            12
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Traits/Competencies
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Available for assessment
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            8
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Accounts
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            In your domain
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#f59e0b',
            marginBottom: '0.5rem'
          }}>
            5
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Reports
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Require your attention
          </p>
        </div>
      </div>

      {/* Action Buttons */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '2rem'
      }}>
        <button 
          className="btn-primary" 
          onClick={handleCreateSurvey}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Survey
        </button>
        <button 
          className="btn-primary" 
          onClick={handleAddTrait}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Add New Trait
        </button>
        <button 
          className="btn-primary" 
          onClick={handleOpenAccount}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Open New Account
        </button>
        <button 
          className="btn-primary" 
          onClick={handleDefineReport}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Define New Report
        </button>
      </div>

      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
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
                        console.log('View report for Team Management Review');
                      }}
                    >
                      View Report
                    </a>
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

        {/* Sidebar */}
        <div>
          {/* AI Insights */}
          <div>
            <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem' }}>
              Domain Analytics
            </h3>
            <div className="card" style={{ padding: '1rem' }}>
              <div style={{ marginBottom: '1rem' }}>
                <h4 style={{ fontSize: '0.875rem', fontWeight: '600', marginBottom: '0.5rem' }}>
                  🎯 Domain Focus Areas
                </h4>
                <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '0.875rem' }}>
                  <li style={{ marginBottom: '0.5rem', color: '#6b7280' }}>
                    • 3 assessees need communication coaching
                  </li>
                  <li style={{ marginBottom: '0.5rem', color: '#6b7280' }}>
                    • 2 leadership assessments ready
                  </li>
                  <li style={{ color: '#6b7280' }}>
                    • 1 learning plan needs review
                  </li>
                </ul>
              </div>
              
              <div>
                <h4 style={{ fontSize: '0.875rem', fontWeight: '600', marginBottom: '0.5rem' }}>
                  📊 Team Trends
                </h4>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.5rem' }}>
                  Most common development area: <strong>Leadership Skills</strong>
                </p>
                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                  Average completion rate: <strong>85%</strong>
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default DomainAdminHome;
