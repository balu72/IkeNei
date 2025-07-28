import { useNavigate } from 'react-router-dom';

const DomainReports = () => {
  const navigate = useNavigate();

  const handleCreateReport = () => {
    console.log('Create New Report clicked');
    navigate('/reports');
  };

  const handleBack = () => {
    navigate('/');
  };

  // Sample reports data - in real app, this would come from API
  const reportsData = [
    {
      id: 1,
      reportName: 'Leadership Development Report',
      reportType: 'Individual Assessment',
      associatedSurvey: 'Leadership Skills Assessment',
      status: 'Active',
      generatedCount: 25,
      lastGenerated: '2024-01-15',
      createdBy: 'Admin User',
      description: 'Comprehensive leadership skills analysis with development recommendations'
    },
    {
      id: 2,
      reportName: 'Team Communication Analysis',
      reportType: 'Team Report',
      associatedSurvey: 'Communication Skills Survey',
      status: 'Active',
      generatedCount: 12,
      lastGenerated: '2024-01-14',
      createdBy: 'Domain Admin',
      description: 'Team-wide communication effectiveness and improvement areas'
    },
    {
      id: 3,
      reportName: 'Project Management Scorecard',
      reportType: 'Performance Report',
      associatedSurvey: 'Project Management Skills',
      status: 'Completed',
      generatedCount: 8,
      lastGenerated: '2024-01-10',
      createdBy: 'Admin User',
      description: 'Project management competency scoring with benchmarks'
    },
    {
      id: 4,
      reportName: 'Quarterly Skills Assessment',
      reportType: 'Aggregate Report',
      associatedSurvey: 'Multiple Surveys',
      status: 'Draft',
      generatedCount: 0,
      lastGenerated: 'Never',
      createdBy: 'Domain Admin',
      description: 'Quarterly overview of all skills assessments across the domain'
    },
    {
      id: 5,
      reportName: '360 Feedback Summary',
      reportType: 'Individual Assessment',
      associatedSurvey: 'Team Management Review',
      status: 'Active',
      generatedCount: 18,
      lastGenerated: '2024-01-12',
      createdBy: 'Admin User',
      description: 'Comprehensive 360-degree feedback analysis with peer insights'
    },
    {
      id: 6,
      reportName: 'Innovation Capability Report',
      reportType: 'Department Report',
      associatedSurvey: 'Innovation & Creativity Assessment',
      status: 'Inactive',
      generatedCount: 3,
      lastGenerated: '2024-01-05',
      createdBy: 'Domain Admin',
      description: 'Department-level innovation and creativity assessment'
    },
    {
      id: 7,
      reportName: 'Learning Path Recommendations',
      reportType: 'Development Report',
      associatedSurvey: 'Multiple Surveys',
      status: 'Active',
      generatedCount: 35,
      lastGenerated: '2024-01-16',
      createdBy: 'Admin User',
      description: 'Personalized learning recommendations based on assessment results'
    },
    {
      id: 8,
      reportName: 'Executive Dashboard',
      reportType: 'Executive Summary',
      associatedSurvey: 'All Active Surveys',
      status: 'Active',
      generatedCount: 5,
      lastGenerated: '2024-01-13',
      createdBy: 'Domain Admin',
      description: 'High-level executive summary of organizational capabilities'
    }
  ];

  const getStatusStyle = (status) => {
    const styles = {
      'Active': {
        backgroundColor: '#dcfce7',
        color: '#166534'
      },
      'Draft': {
        backgroundColor: '#fef3c7',
        color: '#d97706'
      },
      'Completed': {
        backgroundColor: '#fee2e2',
        color: '#dc2626'
      },
      'Inactive': {
        backgroundColor: '#f3f4f6',
        color: '#6b7280'
      }
    };
    
    return {
      ...styles[status],
      padding: '0.25rem 0.75rem',
      borderRadius: '1rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  const getReportTypeStyle = (type) => {
    const colors = {
      'Individual Assessment': '#dbeafe',
      'Team Report': '#fef3c7',
      'Performance Report': '#fee2e2',
      'Aggregate Report': '#f3e8ff',
      'Department Report': '#dcfce7',
      'Development Report': '#fdf4ff',
      'Executive Summary': '#fffbeb'
    };
    
    return {
      backgroundColor: colors[type] || '#f3f4f6',
      color: '#374151',
      padding: '0.25rem 0.5rem',
      borderRadius: '0.375rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  return (
    <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
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
        <h1 className="page-title">Reports Management</h1>
        <p className="page-description">
          Create, manage, and monitor reports generated from survey data. Define report templates and track report generation across your domain.
        </p>
      </div>

      {/* Create Report Button */}
      <div style={{ marginBottom: '2rem', display: 'flex', justifyContent: 'flex-end' }}>
        <button 
          className="btn-primary" 
          onClick={handleCreateReport}
          style={{ 
            padding: '0.75rem 1.5rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Report
        </button>
      </div>

      {/* Reports Table */}
      <div>
        <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
          All Reports
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
                  color: '#374151',
                  minWidth: '200px'
                }}>
                  Report Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '150px'
                }}>
                  Report Type
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '180px'
                }}>
                  Associated Survey
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '100px'
                }}>
                  Status
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Generated Count
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Last Generated
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '100px'
                }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {reportsData.map((report) => (
                <tr key={report.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                  <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                    <div>
                      <div style={{ color: '#374151', fontWeight: '500', marginBottom: '0.25rem' }}>
                        {report.reportName}
                      </div>
                      <div style={{ color: '#6b7280', fontSize: '0.75rem', lineHeight: '1.4' }}>
                        {report.description}
                      </div>
                    </div>
                  </td>
                  <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                    <span style={getReportTypeStyle(report.reportType)}>
                      {report.reportType}
                    </span>
                  </td>
                  <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                    {report.associatedSurvey}
                  </td>
                  <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                    <span style={getStatusStyle(report.status)}>
                      {report.status}
                    </span>
                  </td>
                  <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top', textAlign: 'center' }}>
                    <span style={{
                      backgroundColor: report.generatedCount > 0 ? '#dbeafe' : '#f3f4f6',
                      color: report.generatedCount > 0 ? '#1e40af' : '#6b7280',
                      padding: '0.25rem 0.5rem',
                      borderRadius: '0.375rem',
                      fontSize: '0.75rem',
                      fontWeight: '600'
                    }}>
                      {report.generatedCount}
                    </span>
                  </td>
                  <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top' }}>
                    {report.lastGenerated}
                  </td>
                  <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                    <div style={{ display: 'flex', gap: '0.5rem', flexDirection: 'column' }}>
                      <button
                        onClick={() => console.log('Edit report:', report.id)}
                        style={{
                          padding: '0.25rem 0.5rem',
                          fontSize: '0.75rem',
                          border: '1px solid #d1d5db',
                          borderRadius: '0.25rem',
                          backgroundColor: 'white',
                          color: '#374151',
                          cursor: 'pointer'
                        }}
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => console.log('Generate report:', report.id)}
                        style={{
                          padding: '0.25rem 0.5rem',
                          fontSize: '0.75rem',
                          border: '1px solid #d1d5db',
                          borderRadius: '0.25rem',
                          backgroundColor: '#f0f9ff',
                          color: '#0369a1',
                          cursor: 'pointer'
                        }}
                      >
                        Generate
                      </button>
                      <button
                        onClick={() => console.log('Toggle status:', report.id)}
                        style={{
                          padding: '0.25rem 0.5rem',
                          fontSize: '0.75rem',
                          border: '1px solid #d1d5db',
                          borderRadius: '0.25rem',
                          backgroundColor: report.status === 'Active' ? '#fef3c7' : '#dcfce7',
                          color: report.status === 'Active' ? '#d97706' : '#166534',
                          cursor: 'pointer'
                        }}
                      >
                        {report.status === 'Active' ? 'Deactivate' : 'Activate'}
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
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
            {reportsData.filter(r => r.status === 'Active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Reports</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {reportsData.filter(r => r.status === 'Draft').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Reports</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>
            {reportsData.filter(r => r.status === 'Completed').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Completed Reports</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {reportsData.reduce((sum, r) => sum + r.generatedCount, 0)}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Generated</p>
        </div>
      </div>
    </div>
  );
};

export default DomainReports;
