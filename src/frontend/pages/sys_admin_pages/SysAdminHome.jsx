import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { dashboardAPI, accountsAPI, surveysAPI } from '../../services/api';

const SysAdminHome = () => {
  const navigate = useNavigate();
  const [dashboardData, setDashboardData] = useState({
    totalAccounts: 0,
    activeSurveys: 0,
    systemHealth: '--'
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch dashboard data from API
  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setLoading(true);
        
        // Fetch data from multiple endpoints
        const [statsResponse, accountsResponse, surveysResponse] = await Promise.all([
          dashboardAPI.getStats().catch(() => ({ success: false })),
          accountsAPI.getAll().catch(() => ({ success: false })),
          surveysAPI.getAll().catch(() => ({ success: false }))
        ]);

        const newDashboardData = {
          totalAccounts: 0,
          activeSurveys: 0,
          systemHealth: '--'
        };

        // Debug logging
        console.log('Dashboard API Responses:', {
          statsResponse,
          accountsResponse,
          surveysResponse
        });

        // Use stats API if available, otherwise calculate from individual APIs
        if (statsResponse.success && statsResponse.data && statsResponse.data.totalAccounts !== undefined) {
          newDashboardData.totalAccounts = statsResponse.data.totalAccounts || 0;
          newDashboardData.activeSurveys = statsResponse.data.activeSurveys || 0;
          newDashboardData.systemHealth = statsResponse.data.systemHealth || '--';
        } else {
          // Fallback to individual API responses
          if (accountsResponse.success && accountsResponse.data) {
            newDashboardData.totalAccounts = Array.isArray(accountsResponse.data) ? accountsResponse.data.length : 0;
            console.log('Total accounts calculated:', newDashboardData.totalAccounts);
          }
          if (surveysResponse.success && surveysResponse.data) {
            const surveyData = Array.isArray(surveysResponse.data) ? surveysResponse.data : [];
            const activeSurveys = surveyData.filter(s => s.status === 'active' || s.state === 'Active');
            newDashboardData.activeSurveys = activeSurveys.length;
            console.log('Active surveys calculated:', newDashboardData.activeSurveys, 'from', surveyData.length, 'total surveys');
          }
          newDashboardData.systemHealth = 'Online';
        }

        console.log('Final dashboard data:', newDashboardData);

        setDashboardData(newDashboardData);
      } catch (err) {
        setError(err.message || 'Failed to fetch dashboard data');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);


  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">System Administration</h1>
        <p className="page-description">
          Manage global accounts, configure system-wide settings, and monitor platform-wide analytics for IkeNei.
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
            {loading ? '...' : dashboardData.totalAccounts}
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Total Accounts
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Active platform accounts
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            {loading ? '...' : dashboardData.activeSurveys}
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
            color: '#f59e0b',
            marginBottom: '0.5rem'
          }}>
            {loading ? '...' : dashboardData.systemHealth}
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
          
          <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
            <p style={{ fontSize: '0.875rem', color: '#6b7280', fontStyle: 'italic' }}>
              No recent activity to display. System activity will appear here once the platform is in use.
            </p>
          </div>
        </div>

        {/* Admin Tools Sidebar */}
        <div>
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
                <span style={{ fontSize: '0.875rem', fontWeight: '600' }}>0</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>Feedback Responses</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600' }}>0</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>System Uptime</span>
                <span style={{ fontSize: '0.875rem', fontWeight: '600', color: '#10b981' }}>--</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SysAdminHome;
