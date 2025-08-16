import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { surveysAPI } from '../../services/api';

const Surveys = () => {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterState, setFilterState] = useState('all');
  const [filterSector, setFilterSector] = useState('all');
  const [surveysData, setSurveysData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch surveys data from API
  useEffect(() => {
    const fetchSurveys = async () => {
      try {
        setLoading(true);
        const response = await surveysAPI.getAll();
        if (response.success) {
          setSurveysData(response.data || []);
        } else {
          setError('Failed to fetch surveys');
        }
      } catch (err) {
        setError(err.message || 'Failed to fetch surveys');
      } finally {
        setLoading(false);
      }
    };

    fetchSurveys();
  }, []);

  // Get unique sectors for filter dropdown (using account_name as sector substitute)
  const sectors = [...new Set(surveysData.map(survey => {
    // Handle different possible field names for account/sector
    return survey.account_name || survey.sector || survey.domain || survey.organization || 'Unknown';
  }).filter(Boolean))];

  // Filter surveys based on search term, state filter, and sector filter
  const filteredSurveys = surveysData.filter(survey => {
    const matchesSearch = survey.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         survey.description?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         (survey.account_name && survey.account_name.toLowerCase().includes(searchTerm.toLowerCase()));
    
    const matchesState = filterState === 'all' || survey.status === filterState;
    
    // Improved sector matching with fallback options
    const surveyAccountName = survey.account_name || survey.sector || survey.domain || survey.organization || 'Unknown';
    const matchesSector = filterSector === 'all' || surveyAccountName === filterSector;
    
    return matchesSearch && matchesState && matchesSector;
  });

  const handleBack = () => {
    navigate('/');
  };

  const handleStatusChange = async (surveyId, newStatus) => {
    try {
      const response = await surveysAPI.updateStatus(surveyId, newStatus);
      
      if (response.success) {
        // Update the local state to reflect the change
        setSurveysData(prevData => 
          prevData.map(survey => 
            survey.id === surveyId 
              ? { ...survey, status: newStatus }
              : survey
          )
        );
        alert(`Survey status updated to ${newStatus} successfully!`);
      } else {
        setError('Failed to update survey status');
      }
    } catch (err) {
      setError(err.message || 'Failed to update survey status');
    }
  };

  const getStateStyle = (status) => {
    const styles = {
      'draft': { backgroundColor: '#f3f4f6', color: '#374151' },
      'active': { backgroundColor: '#dcfce7', color: '#166534' },
      'inactive': { backgroundColor: '#fef3c7', color: '#d97706' },
      'completed': { backgroundColor: '#dbeafe', color: '#1e40af' },
      'archived': { backgroundColor: '#f3e8ff', color: '#7c3aed' }
    };
    
    return {
      ...styles[status] || styles['draft'],
      padding: '0.25rem 0.75rem',
      borderRadius: '1rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  const getStatusDisplayName = (status) => {
    const names = {
      'draft': 'Draft',
      'active': 'Active',
      'inactive': 'Inactive',
      'completed': 'Completed',
      'archived': 'Archived'
    };
    return names[status] || status;
  };

  const StatusDropdown = ({ currentStatus, onStatusChange, surveyId }) => {
    const statusOptions = ['draft', 'active', 'inactive', 'completed', 'archived'];
    
    const handleChange = (e) => {
      const newStatus = e.target.value;
      if (newStatus !== currentStatus) {
        onStatusChange(surveyId, newStatus);
      }
    };

    return (
      <select
        value={currentStatus}
        onChange={handleChange}
        style={{
          padding: '0.5rem',
          border: '1px solid #d1d5db',
          borderRadius: '0.375rem',
          fontSize: '0.75rem',
          backgroundColor: 'white',
          color: '#374151',
          cursor: 'pointer',
          minWidth: '100px'
        }}
      >
        {statusOptions.map(status => (
          <option key={status} value={status}>
            {getStatusDisplayName(status)}
          </option>
        ))}
      </select>
    );
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
        <h1 className="page-title">Survey Management</h1>
        <p className="page-description">
          Monitor and manage all platform surveys, control survey states, and oversee survey deployment across sectors.
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
            placeholder="Search surveys..."
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
          
          {/* State Filter */}
          <select
            value={filterState}
            onChange={(e) => setFilterState(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem'
            }}
          >
            <option value="all">All States</option>
            <option value="draft">Draft</option>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
            <option value="completed">Completed</option>
            <option value="archived">Archived</option>
          </select>

          {/* Sector Filter */}
          <select
            value={filterSector}
            onChange={(e) => setFilterSector(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem'
            }}
          >
            <option value="all">All Sectors</option>
            {sectors.map(sector => (
              <option key={sector} value={sector}>{sector}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Surveys Table */}
      <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          padding: '1.5rem',
          borderBottom: '1px solid #e5e7eb'
        }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#374151' }}>
            All Surveys ({filteredSurveys.length})
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
                  Survey Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '300px'
                }}>
                  Traits/Competencies
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Sector
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '100px'
                }}>
                  State
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
              {filteredSurveys.length > 0 ? (
                filteredSurveys.map((survey) => (
                  <tr key={survey.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151', fontWeight: '500', verticalAlign: 'top' }}>
                      {survey.title}
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top', lineHeight: '1.5' }}>
                      {survey.description}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top' }}>
                      <span style={{
                        backgroundColor: '#f3f4f6',
                        color: '#374151',
                        padding: '0.25rem 0.5rem',
                        borderRadius: '0.375rem',
                        fontSize: '0.75rem',
                        fontWeight: '500'
                      }}>
                        {survey.account_name || survey.sector || survey.domain || survey.organization || 'Unknown'}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getStateStyle(survey.status)}>
                        {getStatusDisplayName(survey.status)}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center', flexDirection: 'column' }}>
                        <StatusDropdown 
                          currentStatus={survey.status}
                          onStatusChange={handleStatusChange}
                          surveyId={survey.id}
                        />
                        <button
                          onClick={() => navigate(`/survey-details/${survey.id}`)}
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
                          Details
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" style={{ 
                    padding: '2rem', 
                    textAlign: 'center', 
                    color: '#6b7280',
                    fontStyle: 'italic'
                  }}>
                    No surveys found matching your criteria.
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
        gridTemplateColumns: 'repeat(6, 1fr)', 
        gap: '1rem',
        marginTop: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#374151', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'draft').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#10b981', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'inactive').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Inactive Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#1e40af', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'completed').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Completed Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#7c3aed', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.status === 'archived').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Archived Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#8b5cf6', marginBottom: '0.5rem' }}>
            {surveysData.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Surveys</p>
        </div>
      </div>
    </div>
  );
};

export default Surveys;
