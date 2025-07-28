import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import CreateSubjectModal from '../../components/CreateSubjectModal';
import CreateRespondantModal from '../../components/CreateRespondantModal';

const AccountHome = () => {
  const navigate = useNavigate();
  const [showSubjectModal, setShowSubjectModal] = useState(false);
  const [showRespondantModal, setShowRespondantModal] = useState(false);

  const handleUpdateProfile = () => {
    navigate('/profile');
  };

  const handleCreateSubject = () => {
    setShowSubjectModal(true);
  };

  const handleCreateRespondant = () => {
    setShowRespondantModal(true);
  };


  const handleRunSurvey = () => {
    navigate('/run-survey');
  };

  const handleSubjectSubmit = (data) => {
    console.log('Subject data:', data);
    alert('Subject created successfully!');
    setShowSubjectModal(false);
  };

  const handleRespondantSubmit = (data) => {
    console.log('Respondant data:', data);
    alert('Respondant created successfully!');
    setShowRespondantModal(false);
  };


  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">Account Management Dashboard</h1>
        <p className="page-description">
          Manage your account settings, participate in surveys, and track your feedback responses.
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
            color: '#d946ef',
            marginBottom: '0.5rem'
          }}>
            2
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Subjects
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Taking 360 degree survey.
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#10b981',
            marginBottom: '0.5rem'
          }}>
            3
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Respondants
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Participating in surveys
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            2
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Live Surveys
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Data Collection in Progress
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
          onClick={handleCreateSubject}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Subject
        </button>
        <button 
          className="btn-primary" 
          onClick={handleCreateRespondant}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Respondant
        </button>
        <button 
          className="btn-primary" 
          onClick={handleRunSurvey}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Run Survey
        </button>
      </div>

      {/* Survey Table */}
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
                  Subject
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Respondant
                </th>
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
                  Status
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  View Report
                </th>
              </tr>
            </thead>
            <tbody>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>John Doe</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Sarah Wilson, Mike Johnson, Emily Davis
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Leadership Skills Assessment</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>Jane Smith</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Robert Brown, Lisa Anderson, David Wilson, Tom Harris
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Communication Skills Survey</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#fef3c7',
                    color: '#d97706',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>Robert Brown</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Emily Davis, Sarah Wilson, John Doe
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Team Management Review</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#fee2e2',
                    color: '#dc2626',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Closed
                  </span>
                </td>
                <td style={{ padding: '1rem' }}>
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
                      // Handle report view
                      console.log('View report for Team Management Review');
                    }}
                  >
                    View Report
                  </a>
                </td>
              </tr>
              <tr>
                <td style={{ padding: '1rem', color: '#374151' }}>Lisa Anderson</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  David Wilson, Mike Johnson, Jane Smith, Robert Brown, Sarah Wilson
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Project Management Skills</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal Components */}
      <CreateSubjectModal
        isOpen={showSubjectModal}
        onClose={() => setShowSubjectModal(false)}
        onSubmit={handleSubjectSubmit}
      />

      <CreateRespondantModal
        isOpen={showRespondantModal}
        onClose={() => setShowRespondantModal(false)}
        onSubmit={handleRespondantSubmit}
      />

    </div>
  );
};

export default AccountHome;
