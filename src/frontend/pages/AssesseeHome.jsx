const AssesseeHome = () => {
  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">Welcome to Your Development Journey</h1>
        <p className="page-description">
          Track your 360° feedback, explore AI-powered learning recommendations, and monitor your professional growth.
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
            Active Surveys
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Feedback collection in progress
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
            Learning Plans
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            AI-generated development paths
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            78%
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Progress
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Overall development completion
          </p>
        </div>
      </div>

      {/* Recent Activity */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        {/* Main Content */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Recent Activity
          </h2>
          
          <div className="card" style={{ marginBottom: '1rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{
                width: '3rem',
                height: '3rem',
                backgroundColor: '#fae8ff',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                marginRight: '1rem'
              }}>
                <span style={{ fontSize: '1.5rem' }}>📊</span>
              </div>
              <div>
                <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                  Leadership Skills Assessment
                </h3>
                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                  Feedback collection completed • 12 responses received
                </p>
              </div>
            </div>
            <button className="btn-primary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
              View Results
            </button>
          </div>

          <div className="card">
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{
                width: '3rem',
                height: '3rem',
                backgroundColor: '#dcfce7',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                marginRight: '1rem'
              }}>
                <span style={{ fontSize: '1.5rem' }}>🎯</span>
              </div>
              <div>
                <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                  New Learning Plan Generated
                </h3>
                <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                  AI-powered recommendations based on your feedback
                </p>
              </div>
            </div>
            <button className="btn-secondary" style={{ fontSize: '0.875rem', padding: '0.5rem 1rem' }}>
              Explore Plan
            </button>
          </div>
        </div>

        {/* Sidebar */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Quick Actions
          </h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            <button className="btn-primary" style={{ width: '100%', textAlign: 'left' }}>
              🚀 Start New 360° Survey
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📈 View Progress Report
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              ⚙️ Update Profile
            </button>
          </div>

          {/* Next Steps */}
          <div style={{ marginTop: '2rem' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem' }}>
              Recommended Next Steps
            </h3>
            <div className="card" style={{ padding: '1rem' }}>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                <li style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  marginBottom: '0.75rem',
                  fontSize: '0.875rem'
                }}>
                  <span style={{ marginRight: '0.5rem' }}>✅</span>
                  Complete communication skills module
                </li>
                <li style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  marginBottom: '0.75rem',
                  fontSize: '0.875rem'
                }}>
                  <span style={{ marginRight: '0.5rem' }}>📚</span>
                  Review feedback from team members
                </li>
                <li style={{ 
                  display: 'flex', 
                  alignItems: 'center',
                  fontSize: '0.875rem'
                }}>
                  <span style={{ marginRight: '0.5rem' }}>🎯</span>
                  Set goals for next quarter
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AssesseeHome;
