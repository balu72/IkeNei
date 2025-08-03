import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { reportsAPI } from '../../services/api';

const DomainReports = () => {
  const navigate = useNavigate();
  const [reportsData, setReportsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch reports data from API
  useEffect(() => {
    const fetchReports = async () => {
      try {
        setLoading(true);
        setError(null);
        
        const response = await reportsAPI.getAll();
        
        if (response.success) {
          setReportsData(response.data || []);
        } else {
          setError(response.error?.message || 'Failed to load reports');
        }
        
      } catch (err) {
        console.error('Error fetching reports:', err);
        setError(err.message || 'Failed to load reports');
      } finally {
        setLoading(false);
      }
    };
    
    fetchReports();
  }, []);

  const handleCreateReport = () => {
    console.log('Create New Report clicked');
    navigate('/reports');
  };

  const handleBack = () => {
    navigate('/');
  };

  const handleEditReport = async (reportId) => {
    console.log('Edit report:', reportId);
    // Navigate to edit page or open edit modal
  };

  const handleGenerateReport = async (reportId) => {
    try {
      const response = await reportsAPI.generate(reportId);
      if (response.success) {
        alert('Report generated successfully!');
        // Refresh the reports list to update generated count
        window.location.reload();
      } else {
        alert('Failed to generate report: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (err) {
      console.error('Error generating report:', err);
      alert('Failed to generate report: ' + err.message);
    }
  };

  const handleToggleStatus = async (reportId, currentStatus) => {
    try {
      const newStatus = currentStatus === 'Active' ? 'Inactive' : 'Active';
      const response = await reportsAPI.updateStatus(reportId, newStatus);
      
      if (response.success) {
        // Update local state
        setReportsData(prev => prev.map(report => 
          report.id === reportId ? { ...report, status: newStatus } : report
        ));
      } else {
        alert('Failed to update status: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (err) {
      console.error('Error updating status:', err);
      alert('Failed to update status: ' + err.message);
    }
  };

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

  // Loading state
  if (loading) {
    return (
      <div style={{ maxWidth: '1400px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Reports Management</h1>
        <div style={{ padding: '2rem' }}>
          <p>Loading reports...</p>
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div style={{ maxWidth: '1400px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Reports Management</h1>
        <div style={{ padding: '2rem', color: '#dc2626' }}>
          <p>Error: {error}</p>
          <button 
            onClick={() => window.location.reload()}
            className="btn-primary"
            style={{ marginTop: '1rem' }}
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

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
                        onClick={() => handleEditReport(report.id)}
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
                        onClick={() => handleGenerateReport(report.id)}
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
                        onClick={() => handleToggleStatus(report.id, report.status)}
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
