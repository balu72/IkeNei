import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { traitsAPI } from '../../services/api';

const DomainTraits = () => {
  const navigate = useNavigate();
  const [traitsData, setTraitsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch traits data from API
  useEffect(() => {
    const fetchTraits = async () => {
      try {
        setLoading(true);
        const response = await traitsAPI.getAll();
        if (response.success) {
          setTraitsData(response.data || []);
        } else {
          setError('Failed to fetch traits');
        }
      } catch (err) {
        setError(err.message || 'Failed to fetch traits');
      } finally {
        setLoading(false);
      }
    };

    fetchTraits();
  }, []);

  const handleCreateTrait = () => {
    console.log('Create New Trait clicked');
    navigate('/create-trait');
  };

  const handleBack = () => {
    navigate('/');
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
      'Inactive': {
        backgroundColor: '#fee2e2',
        color: '#dc2626'
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

  const getCategoryStyle = (category) => {
    const colors = {
      'Leadership': '#dbeafe',
      'Communication': '#fef3c7',
      'Analytical': '#fee2e2',
      'Creativity': '#f3e8ff',
      'Personal': '#dcfce7'
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
        <h1 className="page-title">Traits & Competencies</h1>
        <p className="page-description">
          Manage and organize traits and competencies used in surveys. Create new traits and monitor their usage across different assessments.
        </p>
      </div>

      {/* Create Trait Button */}
      <div style={{ marginBottom: '2rem', display: 'flex', justifyContent: 'flex-end' }}>
        <button 
          className="btn-primary" 
          onClick={handleCreateTrait}
          style={{ 
            padding: '0.75rem 1.5rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Trait
        </button>
      </div>

      {/* Traits Table */}
      <div>
        <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
          All Traits & Competencies
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
                  Trait Name
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
                  Status
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151',
                  minWidth: '120px'
                }}>
                  Used in Surveys
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
                  minWidth: '100px'
                }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {traitsData.length > 0 ? (
                traitsData.map((trait) => (
                  <tr key={trait.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151', fontWeight: '500', verticalAlign: 'top' }}>
                      {trait.traitName}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getCategoryStyle(trait.category)}>
                        {trait.category}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top', lineHeight: '1.5' }}>
                      {trait.description}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <span style={getStatusStyle(trait.status)}>
                        {trait.status}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#374151', verticalAlign: 'top', textAlign: 'center' }}>
                      <span style={{
                        backgroundColor: trait.usedInSurveys > 0 ? '#dbeafe' : '#f3f4f6',
                        color: trait.usedInSurveys > 0 ? '#1e40af' : '#6b7280',
                        padding: '0.25rem 0.5rem',
                        borderRadius: '0.375rem',
                        fontSize: '0.75rem',
                        fontWeight: '600'
                      }}>
                        {trait.usedInSurveys}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top' }}>
                      {trait.lastModified}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <div style={{ display: 'flex', gap: '0.5rem', flexDirection: 'column' }}>
                        <button
                          onClick={() => console.log('Edit trait:', trait.id)}
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
                          onClick={() => console.log('Toggle status:', trait.id)}
                          style={{
                            padding: '0.25rem 0.5rem',
                            fontSize: '0.75rem',
                            border: '1px solid #d1d5db',
                            borderRadius: '0.25rem',
                            backgroundColor: trait.status === 'Active' ? '#fef3c7' : '#dcfce7',
                            color: trait.status === 'Active' ? '#d97706' : '#166534',
                            cursor: 'pointer'
                          }}
                        >
                          {trait.status === 'Active' ? 'Deactivate' : 'Activate'}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="7" style={{ 
                    padding: '2rem', 
                    textAlign: 'center', 
                    color: '#6b7280',
                    fontStyle: 'italic'
                  }}>
                    No traits found. Create your first trait to get started.
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
            {traitsData.filter(t => t.status === 'Active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Traits</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {traitsData.filter(t => t.status === 'Draft').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Traits</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>
            {traitsData.filter(t => t.status === 'Inactive').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Inactive Traits</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {[...new Set(traitsData.map(t => t.category))].length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Categories</p>
        </div>
      </div>
    </div>
  );
};

export default DomainTraits;
