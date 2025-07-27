const DomainAdminHome = () => {
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
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            8
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Domain Users
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            In your domain
          </p>
        </div>

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
            Surveys in Progress
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Feedback collection active
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
            Pending Reviews
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Require your attention
          </p>
        </div>
      </div>

      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        {/* Recent Assessee Activity */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Recent User Activity
          </h2>
          
          <div className="card" style={{ marginBottom: '1rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <div style={{
                  width: '3rem',
                  height: '3rem',
                  backgroundColor: '#dbeafe',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginRight: '1rem',
                  fontSize: '1rem',
                  fontWeight: '600',
                  color: '#3b82f6'
                }}>
                  JD
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    John Doe
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    Completed Leadership Assessment • 12 responses
                  </p>
                </div>
              </div>
              <div style={{
                backgroundColor: '#dcfce7',
                color: '#166534',
                padding: '0.25rem 0.75rem',
                borderRadius: '1rem',
                fontSize: '0.75rem',
                fontWeight: '500'
              }}>
                Ready for Review
              </div>
            </div>
            <button className="btn-primary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
              Review Results
            </button>
          </div>

          <div className="card" style={{ marginBottom: '1rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <div style={{
                  width: '3rem',
                  height: '3rem',
                  backgroundColor: '#fef3c7',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginRight: '1rem',
                  fontSize: '1rem',
                  fontWeight: '600',
                  color: '#d97706'
                }}>
                  SM
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    Sarah Miller
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    Communication Skills Survey • 8/15 responses
                  </p>
                </div>
              </div>
              <div style={{
                backgroundColor: '#fef3c7',
                color: '#d97706',
                padding: '0.25rem 0.75rem',
                borderRadius: '1rem',
                fontSize: '0.75rem',
                fontWeight: '500'
              }}>
                In Progress
              </div>
            </div>
            <button className="btn-secondary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
              Send Reminder
            </button>
          </div>

          <div className="card">
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <div style={{
                  width: '3rem',
                  height: '3rem',
                  backgroundColor: '#fae8ff',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginRight: '1rem',
                  fontSize: '1rem',
                  fontWeight: '600',
                  color: '#a21caf'
                }}>
                  RJ
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    Robert Johnson
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    Started new learning plan • Team Management
                  </p>
                </div>
              </div>
              <div style={{
                backgroundColor: '#e0e7ff',
                color: '#3730a3',
                padding: '0.25rem 0.75rem',
                borderRadius: '1rem',
                fontSize: '0.75rem',
                fontWeight: '500'
              }}>
                Learning
              </div>
            </div>
            <button className="btn-secondary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
              View Progress
            </button>
          </div>
        </div>

        {/* Coaching Tools Sidebar */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Admin Tools
          </h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginBottom: '2rem' }}>
            <button className="btn-primary" style={{ width: '100%', textAlign: 'left' }}>
              👥 Manage Users
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📊 Create Survey/Questionnaire
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📈 View Reports
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📋 Domain Reports
            </button>
          </div>

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

          {/* Upcoming Sessions */}
          <div style={{ marginTop: '2rem' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem' }}>
              Upcoming Sessions
            </h3>
            <div className="card" style={{ padding: '1rem' }}>
              <div style={{ marginBottom: '1rem', paddingBottom: '1rem', borderBottom: '1px solid #e5e7eb' }}>
                <div style={{ fontSize: '0.875rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                  John Doe - 1:1 Coaching
                </div>
                <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>
                  Tomorrow, 2:00 PM
                </div>
              </div>
              <div>
                <div style={{ fontSize: '0.875rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                  Team Development Review
                </div>
                <div style={{ fontSize: '0.75rem', color: '#6b7280' }}>
                  Friday, 10:00 AM
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DomainAdminHome;
