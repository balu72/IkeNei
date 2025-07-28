import { useNavigate } from 'react-router-dom';

const DomainTraits = () => {
  const navigate = useNavigate();

  const handleCreateTrait = () => {
    console.log('Create New Trait clicked');
    navigate('/create-trait');
  };

  const handleBack = () => {
    navigate('/');
  };

  // Sample traits data - in real app, this would come from API
  const traitsData = [
    {
      id: 1,
      traitName: 'Strategic Thinking',
      category: 'Leadership',
      description: 'Ability to think long-term and develop comprehensive strategies',
      status: 'Active',
      usedInSurveys: 5,
      lastModified: '2024-01-15'
    },
    {
      id: 2,
      traitName: 'Decision Making',
      category: 'Leadership',
      description: 'Capacity to make effective decisions under pressure',
      status: 'Active',
      usedInSurveys: 4,
      lastModified: '2024-01-12'
    },
    {
      id: 3,
      traitName: 'Team Management',
      category: 'Leadership',
      description: 'Skills in leading and managing team members effectively',
      status: 'Active',
      usedInSurveys: 6,
      lastModified: '2024-01-10'
    },
    {
      id: 4,
      traitName: 'Verbal Communication',
      category: 'Communication',
      description: 'Ability to communicate effectively through spoken words',
      status: 'Active',
      usedInSurveys: 3,
      lastModified: '2024-01-14'
    },
    {
      id: 5,
      traitName: 'Written Communication',
      category: 'Communication',
      description: 'Skills in expressing ideas clearly through written text',
      status: 'Active',
      usedInSurveys: 3,
      lastModified: '2024-01-13'
    },
    {
      id: 6,
      traitName: 'Active Listening',
      category: 'Communication',
      description: 'Ability to listen attentively and understand others',
      status: 'Active',
      usedInSurveys: 2,
      lastModified: '2024-01-11'
    },
    {
      id: 7,
      traitName: 'Problem Solving',
      category: 'Analytical',
      description: 'Capacity to identify and solve complex problems',
      status: 'Draft',
      usedInSurveys: 0,
      lastModified: '2024-01-16'
    },
    {
      id: 8,
      traitName: 'Innovation',
      category: 'Creativity',
      description: 'Ability to generate new ideas and creative solutions',
      status: 'Active',
      usedInSurveys: 2,
      lastModified: '2024-01-09'
    },
    {
      id: 9,
      traitName: 'Adaptability',
      category: 'Personal',
      description: 'Flexibility to adjust to changing circumstances',
      status: 'Active',
      usedInSurveys: 4,
      lastModified: '2024-01-08'
    },
    {
      id: 10,
      traitName: 'Time Management',
      category: 'Personal',
      description: 'Ability to manage time effectively and meet deadlines',
      status: 'Inactive',
      usedInSurveys: 1,
      lastModified: '2024-01-07'
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
              {traitsData.map((trait) => (
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
