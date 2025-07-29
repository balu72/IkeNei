import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Settings = () => {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCategory, setFilterCategory] = useState('all');

  // Sample settings data - in real app, this would come from API
  const [settingsData, setSettingsData] = useState([
    {
      id: 1,
      settingName: 'User Registration',
      category: 'Authentication',
      description: 'Allow new accounts to register',
      value: 'Enabled',
      type: 'boolean',
      lastModified: '2024-01-15'
    },
    {
      id: 2,
      settingName: 'Email Notifications',
      category: 'Communication',
      description: 'Send email notifications for survey completions',
      value: 'Enabled',
      type: 'boolean',
      lastModified: '2024-01-10'
    },
    {
      id: 3,
      settingName: 'Session Timeout',
      category: 'Security',
      description: 'User session timeout duration in minutes',
      value: '30',
      type: 'number',
      lastModified: '2024-01-12'
    },
    {
      id: 4,
      settingName: 'Max Survey Responses',
      category: 'Survey',
      description: 'Maximum number of responses per survey',
      value: '1000',
      type: 'number',
      lastModified: '2024-01-08'
    },
    {
      id: 5,
      settingName: 'Data Backup Frequency',
      category: 'System',
      description: 'Automatic backup frequency in hours',
      value: '24',
      type: 'number',
      lastModified: '2024-01-14'
    },
    {
      id: 6,
      settingName: 'Password Complexity',
      category: 'Security',
      description: 'Enforce strong password requirements',
      value: 'Enabled',
      type: 'boolean',
      lastModified: '2024-01-11'
    },
    {
      id: 7,
      settingName: 'Survey Auto-Archive',
      category: 'Survey',
      description: 'Automatically archive completed surveys after days',
      value: '90',
      type: 'number',
      lastModified: '2024-01-09'
    },
    {
      id: 8,
      settingName: 'API Rate Limiting',
      category: 'System',
      description: 'Enable API rate limiting for external requests',
      value: 'Enabled',
      type: 'boolean',
      lastModified: '2024-01-13'
    },
    {
      id: 9,
      settingName: 'Maintenance Mode',
      category: 'System',
      description: 'Enable maintenance mode for system updates',
      value: 'Disabled',
      type: 'boolean',
      lastModified: '2024-01-16'
    },
    {
      id: 10,
      settingName: 'Default Survey Duration',
      category: 'Survey',
      description: 'Default survey duration in days',
      value: '14',
      type: 'number',
      lastModified: '2024-01-07'
    }
  ]);

  // Get unique categories for filter dropdown
  const categories = [...new Set(settingsData.map(setting => setting.category))];

  // Filter settings based on search term and category filter
  const filteredSettings = settingsData.filter(setting => {
    const matchesSearch = setting.settingName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         setting.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         setting.category.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesCategory = filterCategory === 'all' || setting.category === filterCategory;
    
    return matchesSearch && matchesCategory;
  });

  const handleBack = () => {
    navigate('/');
  };

  const handleToggleSetting = (settingId) => {
    setSettingsData(prevSettings => 
      prevSettings.map(setting => {
        if (setting.id === settingId && setting.type === 'boolean') {
          const newValue = setting.value === 'Enabled' ? 'Disabled' : 'Enabled';
          return {
            ...setting,
            value: newValue,
            lastModified: new Date().toISOString().split('T')[0]
          };
        }
        return setting;
      })
    );
  };

  const handleEditSetting = (settingId) => {
    const setting = settingsData.find(s => s.id === settingId);
    if (setting && setting.type === 'number') {
      const newValue = prompt(`Enter new value for ${setting.settingName}:`, setting.value);
      if (newValue !== null && !isNaN(newValue) && newValue.trim() !== '') {
        setSettingsData(prevSettings => 
          prevSettings.map(s => 
            s.id === settingId 
              ? { ...s, value: newValue.trim(), lastModified: new Date().toISOString().split('T')[0] }
              : s
          )
        );
      }
    }
  };

  const getValueStyle = (type, value) => {
    if (type === 'boolean') {
      return {
        backgroundColor: value === 'Enabled' ? '#dcfce7' : '#fef3c7',
        color: value === 'Enabled' ? '#166534' : '#d97706',
        padding: '0.25rem 0.75rem',
        borderRadius: '1rem',
        fontSize: '0.75rem',
        fontWeight: '500'
      };
    }
    return {
      backgroundColor: '#f3f4f6',
      color: '#374151',
      padding: '0.25rem 0.5rem',
      borderRadius: '0.375rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  const getCategoryStyle = (category) => {
    const colors = {
      'Authentication': '#dbeafe',
      'Communication': '#fef3c7',
      'Security': '#fee2e2',
      'Survey': '#dcfce7',
      'System': '#f3e8ff'
    };
    return {
      backgroundColor: colors[category] || '#f3f4f6',
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
        <h1 className="page-title">System Settings</h1>
        <p className="page-description">
          Configure and manage system-wide settings, security parameters, and operational preferences for the IkeNei platform.
        </p>
      </div>

      {/* Controls */}
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        marginBottom: '2rem',
        gap: '1rem',
        flexWrap: 'wrap'
      }}>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', flex: 1 }}>
          {/* Search */}
          <input
            type="text"
            placeholder="Search settings..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem',
              minWidth: '250px'
            }}
          />
          
          {/* Category Filter */}
          <select
            value={filterCategory}
            onChange={(e) => setFilterCategory(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem'
            }}
          >
            <option value="all">All Categories</option>
            {categories.map(category => (
              <option key={category} value={category}>{category}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Settings Table */}
      <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          padding: '1.5rem',
          borderBottom: '1px solid #e5e7eb'
        }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#374151' }}>
            System Configuration ({filteredSettings.length})
          </h2>
        </div>

        <div style={{ overflow: 'auto' }}>
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
                  Setting Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Category
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '300px'
                }}>
                  Description
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '100px'
                }}>
                  Current Value
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Last Modified
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {filteredSettings.length > 0 ? (
                filteredSettings.map((setting) => (
                  <tr key={setting.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151', fontWeight: '500', verticalAlign: 'top' }}>
                      {setting.settingName}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getCategoryStyle(setting.category)}>
                        {setting.category}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top', lineHeight: '1.5' }}>
                      {setting.description}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getValueStyle(setting.type, setting.value)}>
                        {setting.value}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top' }}>
                      {setting.lastModified}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <div style={{ display: 'flex', gap: '0.5rem', flexDirection: 'column' }}>
                        {setting.type === 'boolean' ? (
                          <button
                            onClick={() => handleToggleSetting(setting.id)}
                            style={{
                              padding: '0.25rem 0.5rem',
                              fontSize: '0.75rem',
                              border: '1px solid #d1d5db',
                              borderRadius: '0.25rem',
                              backgroundColor: setting.value === 'Enabled' ? '#fef3c7' : '#dcfce7',
                              color: setting.value === 'Enabled' ? '#d97706' : '#166534',
                              cursor: 'pointer'
                            }}
                          >
                            {setting.value === 'Enabled' ? 'Disable' : 'Enable'}
                          </button>
                        ) : (
                          <button
                            onClick={() => handleEditSetting(setting.id)}
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
                        )}
                        <button
                          onClick={() => console.log('Reset to default:', setting.id)}
                          style={{
                            padding: '0.25rem 0.5rem',
                            fontSize: '0.75rem',
                            border: '1px solid #d1d5db',
                            borderRadius: '0.25rem',
                            backgroundColor: '#f9fafb',
                            color: '#6b7280',
                            cursor: 'pointer'
                          }}
                        >
                          Reset
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" style={{ 
                    padding: '2rem', 
                    textAlign: 'center', 
                    color: '#6b7280',
                    fontStyle: 'italic'
                  }}>
                    No settings found matching your criteria.
                  </td>
                </tr>
              )}
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
            {settingsData.filter(s => s.type === 'boolean' && s.value === 'Enabled').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Enabled Features</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {settingsData.filter(s => s.type === 'boolean' && s.value === 'Disabled').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Disabled Features</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {categories.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Setting Categories</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#8b5cf6', marginBottom: '0.5rem' }}>
            {settingsData.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Settings</p>
        </div>
      </div>
    </div>
  );
};

export default Settings;
