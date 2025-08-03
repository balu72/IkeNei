import { useState, useEffect } from 'react';
import { surveysAPI, traitsAPI, accountsAPI, reportsAPI, dashboardAPI } from '../../services/api';

const DomainAdminHome = () => {
  const [stats, setStats] = useState({
    surveys: 0,
    traits: 0,
    accounts: 0,
    reports: 0
  });
  const [analytics, setAnalytics] = useState({
    focusAreas: [],
    teamTrends: {
      commonDevelopmentArea: 'Loading...',
      completionRate: 0
    },
    recentActivity: {
      surveysCreated: 0,
      reportsGenerated: 0,
      traitsAdded: 0
    }
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setLoading(true);
        setError(null);

        // Fetch all data in parallel
        const [
          surveysResponse,
          traitsResponse,
          accountsResponse,
          reportsResponse,
          dashboardResponse
        ] = await Promise.allSettled([
          surveysAPI.getAll(),
          traitsAPI.getAll(),
          accountsAPI.getAll(),
          reportsAPI.getAll(),
          dashboardAPI.getStats()
        ]);

        // Process surveys data
        const surveysCount = surveysResponse.status === 'fulfilled' && surveysResponse.value.success 
          ? surveysResponse.value.data?.length || 0 
          : 0;

        // Process traits data
        const traitsCount = traitsResponse.status === 'fulfilled' && traitsResponse.value.success 
          ? traitsResponse.value.data?.length || 0 
          : 0;

        // Process accounts data
        const accountsCount = accountsResponse.status === 'fulfilled' && accountsResponse.value.success 
          ? accountsResponse.value.data?.length || 0 
          : 0;

        // Process reports data
        const reportsCount = reportsResponse.status === 'fulfilled' && reportsResponse.value.success 
          ? reportsResponse.value.data?.length || 0 
          : 0;

        // Update stats
        setStats({
          surveys: surveysCount,
          traits: traitsCount,
          accounts: accountsCount,
          reports: reportsCount
        });

        // Process dashboard analytics - only use real API data, no fallbacks
        if (dashboardResponse.status === 'fulfilled' && dashboardResponse.value.success && dashboardResponse.value.data) {
          const dashboardData = dashboardResponse.value.data;
          setAnalytics({
            focusAreas: dashboardData.focusAreas || [],
            teamTrends: {
              commonDevelopmentArea: dashboardData.commonDevelopmentArea || 'No data available',
              completionRate: dashboardData.completionRate || 0
            },
            recentActivity: {
              surveysCreated: dashboardData.surveysCreatedThisWeek || 0,
              reportsGenerated: dashboardData.reportsGeneratedThisWeek || 0,
              traitsAdded: dashboardData.traitsAddedThisWeek || 0
            }
          });
        } else {
          // Dashboard API failed or returned no data - show only empty states
          console.log('Dashboard API failed or returned no data:', dashboardResponse);
          setAnalytics({
            focusAreas: [], // Empty - will show "No focus areas identified yet"
            teamTrends: {
              commonDevelopmentArea: 'No data available',
              completionRate: 0
            },
            recentActivity: {
              surveysCreated: 0,
              reportsGenerated: 0,
              traitsAdded: 0
            }
          });
        }

      } catch (err) {
        console.error('Error fetching dashboard data:', err);
        setError('Failed to load dashboard data. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return (
      <div style={{ maxWidth: '1200px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <div style={{
          width: '3rem',
          height: '3rem',
          border: '3px solid #d946ef',
          borderTop: '3px solid transparent',
          borderRadius: '50%',
          animation: 'spin 1s linear infinite',
          margin: '0 auto 1rem'
        }}></div>
        <p style={{ color: '#6b7280' }}>Loading dashboard data...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ maxWidth: '1200px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <div style={{ color: '#ef4444', marginBottom: '1rem' }}>⚠️ {error}</div>
        <button 
          onClick={() => window.location.reload()} 
          style={{
            padding: '0.5rem 1rem',
            backgroundColor: '#d946ef',
            color: 'white',
            border: 'none',
            borderRadius: '0.375rem',
            cursor: 'pointer'
          }}
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">Domain Admin Dashboard</h1>
        <p className="page-description">
          Create and manage surveys/questionnaires, oversee domain accounts, and analyze feedback data.
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
            {stats.surveys}
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
            {stats.traits}
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
            {stats.accounts}
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
            {stats.reports}
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
                {analytics.focusAreas.map((area, index) => (
                  <li key={index} style={{ marginBottom: '0.75rem', color: '#6b7280', display: 'flex', alignItems: 'center' }}>
                    <span style={{ 
                      width: '6px', 
                      height: '6px', 
                      backgroundColor: area.priority === 'high' ? '#ef4444' : '#f59e0b', 
                      borderRadius: '50%', 
                      marginRight: '0.5rem' 
                    }}></span>
                    {area.count} {area.area}
                  </li>
                ))}
                {analytics.focusAreas.length === 0 && (
                  <li style={{ color: '#6b7280', fontStyle: 'italic' }}>
                    No focus areas identified yet
                  </li>
                )}
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
                  {analytics.teamTrends.commonDevelopmentArea}
                </p>
              </div>
              <div>
                <p style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.5rem' }}>
                  Average completion rate:
                </p>
                <p style={{ fontSize: '1rem', fontWeight: '600', color: '#10b981' }}>
                  {analytics.teamTrends.completionRate}%
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
                  <span style={{ fontWeight: '600', color: '#374151' }}>
                    {analytics.recentActivity.surveysCreated} this week
                  </span>
                </div>
                <div style={{ marginBottom: '0.75rem', display: 'flex', justifyContent: 'space-between' }}>
                  <span>Reports Generated</span>
                  <span style={{ fontWeight: '600', color: '#374151' }}>
                    {analytics.recentActivity.reportsGenerated} this week
                  </span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>Traits Added</span>
                  <span style={{ fontWeight: '600', color: '#374151' }}>
                    {analytics.recentActivity.traitsAdded} this week
                  </span>
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
