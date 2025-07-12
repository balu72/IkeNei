const AdminHome = () => {
  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">System Administration</h1>
        <p className="page-description">
          Manage users, configure system settings, and monitor platform-wide analytics for 360+AI Planner.
        </p>
      </div>

      {/* System Stats */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#ef4444',
            marginBottom: '0.5rem'
          }}>
            247
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Total Users
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Active platform users
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            89
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Active Surveys
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Currently running
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#10b981',
            marginBottom: '0.5rem'
          }}>
            156
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Learning Plans
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            AI-generated this month
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#f59e0b',
            marginBottom: '0.5rem'
          }}>
            92%
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            System Health
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Overall performance
          </p>
        </div>
      </div>

      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        {/* Recent System Activity */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Recent System Activity
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
                  marginRight: '1rem'
                }}>
                  <span style={{ fontSize: '1.5rem' }}>👥</span>
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    New User Registrations
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    15 new users joined today • 8 Assessees, 5 Coaches, 2 Admins
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
                +15 Today
              </div>
            </div>
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
                  marginRight: '1rem'
                }}>
                  <span style={{ fontSize: '1.5rem' }}>⚠️</span>
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    System Alert
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    Database backup completed • Next backup in 23 hours
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
                Resolved
              </div>
            </div>
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
                  marginRight: '1rem'
                }}>
                  <span style={{ fontSize: '1.5rem' }}>🤖</span>
                </div>
                <div>
                  <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
                    AI Model Update
                  </h3>
                  <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    Learning recommendation engine updated • v2.1.3
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
                Deployed
              </div>
            </div>
          </div>
        </div>

        {/* Admin Tools Sidebar */}
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
            Admin Tools
          </h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginBottom: '2rem' }}>
            <button className="btn-primary" style={{ width: '100%', textAlign: 'left' }}>
              👥 User Management
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              ⚙️ System Settings
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📊 Analytics Dashboard
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              📝 Form Templates
            </button>
            <button className="btn-secondary" style={{ width: '100%', textAlign: 'left' }}>
              🔧 System Maintenance
            </button>
          </div>

          {/* System Health */}
          <div>
            <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem' }}>
              System Health
            </h3>
            <div className="card" style={{ padding: '1rem' }}>
              <div style={{ marginBottom: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>Server Performance</span>
                  <span style={{ fontSize: '0.875rem', color: '#10b981', fontWeight: '600' }}>98%</span>
                </div>
                <div style={{ 
                  width: '100%', 
                  height: '0.5rem', 
                  backgroundColor: '#e5e7eb', 
                  borderRadius: '0.25rem',
                  overflow: 'hidden'
                }}>
                  <div style={{ 
                    width: '98%', 
                    height: '100%', 
                    backgroundColor: '#10b981' 
                  }}></div>
                </div>
              </div>

              <div style={{ marginBottom: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>Database Health</span>
                  <span style={{ fontSize: '0.875rem', color: '#10b981', fontWeight: '600' }}>95%</span>
                </div>
                <div style={{ 
                  width: '100%', 
                  height: '0.5rem', 
                  backgroundColor: '#e5e7eb', 
                  borderRadius: '0.25rem',
                  overflow: 'hidden'
                }}>
                  <div style={{ 
                    width: '95%', 
                    height: '100%', 
                    backgroundColor: '#10b981' 
                  }}></div>
                </div>
              </div>

              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>AI Service</span>
                  <span style={{ fontSize: '0.875rem', color: '#f59e0b', fontWeight: '600' }}>87%</span>
                </div>
                <div style={{ 
                  width: '100%', 
                  height: '0.5rem', 
                  backgroundColor: '#e5e7eb', 
                  borderRadius: '0.25rem',
                  overflow: 'hidden'
                }}>
                  <div style={{ 
                    width: '87%', 
                    height: '100%', 
                    backgroundColor: '#f59e0b' 
                  }}></div>
                </div>
              </div>
            </div>
          </div>

          {/* Quick Stats */}
          <div style={{ marginTop: '2rem' }}>
            <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '1rem' }}>
              Today's Summary
            </h3>
            <div className="card" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>New Surveys Created</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600' }}>12</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>Feedback Responses</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600' }}>89</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>Learning Plans Generated</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600' }}>7</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>System Uptime</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600', color: '#10b981' }}>99.9%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminHome;
