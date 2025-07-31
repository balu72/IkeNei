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

  // Get unique sectors for filter dropdown
  const sectors = [...new Set(surveysData.map(survey => survey.sector))];

  // Filter surveys based on search term, state filter, and sector filter
  const filteredSurveys = surveysData.filter(survey => {
    const matchesSearch = survey.surveyName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         survey.traitsCompetencies.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         survey.sector.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesState = filterState === 'all' || survey.state.toLowerCase() === filterState.toLowerCase();
    const matchesSector = filterSector === 'all' || survey.sector === filterSector;
    
    return matchesSearch && matchesState && matchesSector;
  });

  const handleBack = () => {
    navigate('/');
  };

  const handleToggleState = (surveyId, currentState) => {
    console.log(`Toggle survey ${surveyId} from ${currentState} to ${currentState === 'Active' ? 'Passive' : 'Active'}`);
    // In real app, this would make an API call to update the survey state
    alert(`Survey ${currentState === 'Active' ? 'retired' : 'activated'} successfully!`);
  };

  const getStateStyle = (state) => {
    return {
      backgroundColor: state === 'Active' ? '#dcfce7' : '#fef3c7',
      color: state === 'Active' ? '#166534' : '#d97706',
      padding: '0.25rem 0.75rem',
      borderRadius: '1rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  const getToggleButtonStyle = (state) => {
    return {
      padding: '0.25rem 0.5rem',
      fontSize: '0.75rem',
      border: '1px solid #d1d5db',
      borderRadius: '0.25rem',
      backgroundColor: state === 'Active' ? '#fef3c7' : '#dcfce7',
      color: state === 'Active' ? '#d97706' : '#166534',
      cursor: 'pointer'
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
            <option value="active">Active</option>
            <option value="passive">Passive</option>
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
                      {survey.surveyName}
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top', lineHeight: '1.5' }}>
                      {survey.traitsCompetencies}
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
                        {survey.sector}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getStateStyle(survey.state)}>
                        {survey.state}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <div style={{ display: 'flex', gap: '0.5rem', flexDirection: 'column' }}>
                        <button
                          onClick={() => handleToggleState(survey.id, survey.state)}
                          style={getToggleButtonStyle(survey.state)}
                        >
                          {survey.state === 'Active' ? 'Retire' : 'Activate'}
                        </button>
                        <button
                          onClick={() => console.log('View details:', survey.id)}
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
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1rem',
        marginTop: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#10b981', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.state === 'Active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {surveysData.filter(s => s.state === 'Passive').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Retired Surveys</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {sectors.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Sectors</p>
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
