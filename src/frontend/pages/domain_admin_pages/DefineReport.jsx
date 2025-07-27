import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const DefineReport = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    reportName: '',
    description: '',
    reportType: '',
    dataSource: '',
    selectedSurveys: [],
    selectedTraits: [],
    selectedAccounts: [],
    dateRange: {
      startDate: '',
      endDate: ''
    },
    groupBy: '',
    chartType: '',
    includeComparisons: false,
    includeStatistics: true,
    includeComments: false,
    outputFormat: 'pdf',
    scheduledDelivery: {
      enabled: false,
      frequency: '',
      recipients: []
    }
  });

  // Sample data - in real app, this would come from API
  const reportTypes = [
    'Individual Performance Report',
    'Team Performance Summary',
    'Survey Response Analysis',
    'Trait Competency Report',
    'Comparative Analysis Report',
    'Progress Tracking Report',
    'Custom Dashboard Report'
  ];

  const dataSources = [
    'All Survey Data',
    'Specific Survey Results',
    'Trait-based Analysis',
    'Account Performance',
    'Time-based Trends'
  ];

  const surveys = [
    'Leadership Skills Assessment',
    'Communication Skills Survey',
    'Team Management Review',
    'Project Management Skills'
  ];

  const traits = [
    'Strategic Thinking',
    'Decision Making',
    'Team Management',
    'Verbal Communication',
    'Written Communication',
    'Active Listening',
    'Presentation Skills',
    'Delegation',
    'Conflict Resolution',
    'Performance Management'
  ];

  const accounts = [
    'John Doe',
    'Jane Smith',
    'Robert Brown',
    'Lisa Anderson',
    'Mike Johnson',
    'Sarah Wilson'
  ];

  const chartTypes = [
    'Bar Chart',
    'Line Chart',
    'Pie Chart',
    'Radar Chart',
    'Heatmap',
    'Scatter Plot',
    'Table View'
  ];

  const groupByOptions = [
    'Individual',
    'Department',
    'Role',
    'Survey',
    'Trait',
    'Date Range'
  ];

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (name.includes('.')) {
      const [parent, child] = name.split('.');
      setFormData(prev => ({
        ...prev,
        [parent]: {
          ...prev[parent],
          [child]: type === 'checkbox' ? checked : value
        }
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: type === 'checkbox' ? checked : value
      }));
    }
  };

  const handleMultiSelect = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: prev[field].includes(value)
        ? prev[field].filter(item => item !== value)
        : [...prev[field], value]
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Validation
    if (!formData.reportName.trim()) {
      alert('Please enter a report name');
      return;
    }
    if (!formData.reportType) {
      alert('Please select a report type');
      return;
    }
    if (!formData.dataSource) {
      alert('Please select a data source');
      return;
    }
    if (!formData.chartType) {
      alert('Please select a chart type');
      return;
    }

    console.log('Report definition:', formData);
    alert('Report defined successfully!');
    navigate('/');
  };

  const handleCancel = () => {
    navigate('/');
  };

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <button 
          onClick={handleCancel}
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
        <h1 className="page-title">Define New Report</h1>
        <p className="page-description">
          Create a custom report with specific data sources, visualizations, and delivery options.
        </p>
      </div>

      {/* Define Report Form */}
      <div className="card">
        <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
          {/* Basic Information */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              Basic Information
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Report Name *
                </label>
                <input
                  type="text"
                  name="reportName"
                  value={formData.reportName}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                  placeholder="Enter report name"
                />
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Report Type *
                </label>
                <select
                  name="reportType"
                  value={formData.reportType}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="">Select report type</option>
                  {reportTypes.map((type) => (
                    <option key={type} value={type}>{type}</option>
                  ))}
                </select>
              </div>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                Description
              </label>
              <textarea
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                rows={3}
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  fontSize: '0.875rem',
                  resize: 'vertical'
                }}
                placeholder="Describe the purpose and scope of this report"
              />
            </div>
          </div>

          {/* Data Configuration */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              Data Configuration
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Data Source *
                </label>
                <select
                  name="dataSource"
                  value={formData.dataSource}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="">Select data source</option>
                  {dataSources.map((source) => (
                    <option key={source} value={source}>{source}</option>
                  ))}
                </select>
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Group By
                </label>
                <select
                  name="groupBy"
                  value={formData.groupBy}
                  onChange={handleInputChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="">Select grouping</option>
                  {groupByOptions.map((option) => (
                    <option key={option} value={option}>{option}</option>
                  ))}
                </select>
              </div>
            </div>

            {/* Date Range */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Start Date
                </label>
                <input
                  type="date"
                  name="dateRange.startDate"
                  value={formData.dateRange.startDate}
                  onChange={handleInputChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                />
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  End Date
                </label>
                <input
                  type="date"
                  name="dateRange.endDate"
                  value={formData.dateRange.endDate}
                  onChange={handleInputChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                />
              </div>
            </div>
          </div>

          {/* Data Selection */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              Data Selection
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
              {/* Surveys */}
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Include Surveys
                </label>
                <div style={{
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  padding: '0.75rem',
                  maxHeight: '150px',
                  overflow: 'auto',
                  backgroundColor: '#fafafa'
                }}>
                  {surveys.map((survey) => (
                    <label key={survey} style={{
                      display: 'flex',
                      alignItems: 'center',
                      marginBottom: '0.5rem',
                      cursor: 'pointer'
                    }}>
                      <input
                        type="checkbox"
                        checked={formData.selectedSurveys.includes(survey)}
                        onChange={() => handleMultiSelect('selectedSurveys', survey)}
                        style={{ marginRight: '0.5rem' }}
                      />
                      <span style={{ fontSize: '0.75rem' }}>{survey}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Traits */}
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Include Traits
                </label>
                <div style={{
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  padding: '0.75rem',
                  maxHeight: '150px',
                  overflow: 'auto',
                  backgroundColor: '#fafafa'
                }}>
                  {traits.map((trait) => (
                    <label key={trait} style={{
                      display: 'flex',
                      alignItems: 'center',
                      marginBottom: '0.5rem',
                      cursor: 'pointer'
                    }}>
                      <input
                        type="checkbox"
                        checked={formData.selectedTraits.includes(trait)}
                        onChange={() => handleMultiSelect('selectedTraits', trait)}
                        style={{ marginRight: '0.5rem' }}
                      />
                      <span style={{ fontSize: '0.75rem' }}>{trait}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Accounts */}
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Include Accounts
                </label>
                <div style={{
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  padding: '0.75rem',
                  maxHeight: '150px',
                  overflow: 'auto',
                  backgroundColor: '#fafafa'
                }}>
                  {accounts.map((account) => (
                    <label key={account} style={{
                      display: 'flex',
                      alignItems: 'center',
                      marginBottom: '0.5rem',
                      cursor: 'pointer'
                    }}>
                      <input
                        type="checkbox"
                        checked={formData.selectedAccounts.includes(account)}
                        onChange={() => handleMultiSelect('selectedAccounts', account)}
                        style={{ marginRight: '0.5rem' }}
                      />
                      <span style={{ fontSize: '0.75rem' }}>{account}</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Visualization & Output */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              Visualization & Output
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Chart Type *
                </label>
                <select
                  name="chartType"
                  value={formData.chartType}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="">Select chart type</option>
                  {chartTypes.map((type) => (
                    <option key={type} value={type}>{type}</option>
                  ))}
                </select>
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Output Format
                </label>
                <select
                  name="outputFormat"
                  value={formData.outputFormat}
                  onChange={handleInputChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="pdf">PDF</option>
                  <option value="excel">Excel</option>
                  <option value="csv">CSV</option>
                  <option value="powerpoint">PowerPoint</option>
                </select>
              </div>
            </div>

            {/* Report Options */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
              <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  name="includeComparisons"
                  checked={formData.includeComparisons}
                  onChange={handleInputChange}
                  style={{ marginRight: '0.5rem' }}
                />
                <span style={{ fontSize: '0.875rem' }}>Include Comparisons</span>
              </label>
              
              <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  name="includeStatistics"
                  checked={formData.includeStatistics}
                  onChange={handleInputChange}
                  style={{ marginRight: '0.5rem' }}
                />
                <span style={{ fontSize: '0.875rem' }}>Include Statistics</span>
              </label>
              
              <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  name="includeComments"
                  checked={formData.includeComments}
                  onChange={handleInputChange}
                  style={{ marginRight: '0.5rem' }}
                />
                <span style={{ fontSize: '0.875rem' }}>Include Comments</span>
              </label>
            </div>
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end' }}>
            <button
              type="button"
              onClick={handleCancel}
              className="btn-secondary"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
            >
              Define Report
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default DefineReport;
