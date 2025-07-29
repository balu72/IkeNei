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


      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '2rem' }}>
        {/* Domain Analytics - Full Width */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Domain Analytics
          </h2>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
            {/* Domain Focus Areas */}
            <div className="card" style={{ padding: '1.5rem' }}>
              <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem', display: 'flex', alignItems: 'center' }}>
                🎯 Domain Focus Areas
              </h3>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '0.875rem' }}>
                <li style={{ marginBottom: '0.75rem', color: '#6b7280', display: 'flex', alignItems: 'center' }}>
                  <span style={{ width: '6px', height: '6px', backgroundColor: '#ef4444', borderRadius: '50%', marginRight: '0.5rem' }}></span>
                  3 assessees need communication coaching
                </li>
                <li style={{ marginBottom: '0.75rem', color: '#6b7280', display: 'flex', alignItems: 'center' }}>
                  <span style={{ width: '6px', height: '6px', backgroundColor: '#f59e0b', borderRadius: '50%', marginRight: '0.5rem' }}></span>
                  2 leadership assessments ready
                </li>
              </ul>
            </div>

            {/* Team Trends */}
            <div className="card" style={{ padding: '1.5rem' }}>
              <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem', display: 'flex', alignItems: 'center' }}>
                📊 Team Trends
              </h3>
              <div style={{ marginBottom: '1rem' }}>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.5rem' }}>
                  Most common development area:
                </p>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#374151' }}>
                  Leadership Skills
                </p>
              </div>
              <div>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.5rem' }}>
                  Average completion rate:
                </p>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#10b981' }}>
                  85%
                </p>
              </div>
            </div>

            {/* Recent Activity */}
            <div className="card" style={{ padding: '1.5rem' }}>
              <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem', display: 'flex', alignItems: 'center' }}>
                📈 Recent Activity
              </h3>
              <div style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                <div style={{ marginBottom: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                  <span>Surveys Created</span>
                  <span style={{ fontWeight: '600', color: '#374151' }}>3 this week</span>
                </div>
                <div style={{ marginBottom: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                  <span>Reports Generated</span>
                  <span style={{ fontWeight: '600', color: '#374151' }}>5 this week</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>Traits Added</span>
                  <span style={{ fontWeight: '600', color: '#374151' }}>2 this week</span>
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
