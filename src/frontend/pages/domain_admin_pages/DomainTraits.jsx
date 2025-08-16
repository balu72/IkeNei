import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { traitsAPI } from '../../services/api';

const DomainTraits = () => {
  const navigate = useNavigate();
  const [traitsData, setTraitsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingTrait, setEditingTrait] = useState(null);
  const [showEditModal, setShowEditModal] = useState(false);

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

  const handleToggleStatus = async (traitId, currentStatus) => {
    try {
      const newStatus = currentStatus === 'active' ? 'inactive' : 'active';
      const response = await traitsAPI.updateStatus(traitId, newStatus);
      
      if (response.success) {
        // Update the local state to reflect the change
        setTraitsData(prevData => 
          prevData.map(trait => 
            trait.id === traitId 
              ? { ...trait, status: newStatus }
              : trait
          )
        );
      } else {
        alert('Failed to update trait status: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error toggling trait status:', error);
      alert('Failed to update trait status: ' + error.message);
    }
  };

  const handleEditTrait = async (traitId) => {
    try {
      // Fetch the trait data for editing
      const response = await traitsAPI.getById(traitId);
      if (response.success) {
        setEditingTrait(response.data);
        setShowEditModal(true);
      } else {
        alert('Failed to fetch trait data: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error fetching trait data:', error);
      alert('Failed to fetch trait data: ' + error.message);
    }
  };

  const handleSaveEdit = async (updatedTraitData) => {
    try {
      const response = await traitsAPI.update(editingTrait.id, updatedTraitData);
      if (response.success) {
        // Update the local state
        setTraitsData(prevData => 
          prevData.map(trait => 
            trait.id === editingTrait.id 
              ? response.data
              : trait
          )
        );
        setShowEditModal(false);
        setEditingTrait(null);
        alert('Trait updated successfully!');
      } else {
        alert('Failed to update trait: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error updating trait:', error);
      alert('Failed to update trait: ' + error.message);
    }
  };

  const handleCloseEditModal = () => {
    setShowEditModal(false);
    setEditingTrait(null);
  };

  const getStatusStyle = (status) => {
    const styles = {
      'active': {
        backgroundColor: '#dcfce7',
        color: '#166534'
      },
      'draft': {
        backgroundColor: '#fef3c7',
        color: '#d97706'
      },
      'inactive': {
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
                      {trait.name}
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
                        backgroundColor: (trait.usage_count || 0) > 0 ? '#dbeafe' : '#f3f4f6',
                        color: (trait.usage_count || 0) > 0 ? '#1e40af' : '#6b7280',
                        padding: '0.25rem 0.5rem',
                        borderRadius: '0.375rem',
                        fontSize: '0.75rem',
                        fontWeight: '600'
                      }}>
                        {trait.usage_count || 0}
                      </span>
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280', verticalAlign: 'top' }}>
                      {trait.updated_at ? new Date(trait.updated_at).toLocaleDateString() : 'N/A'}
                    </td>
                    <td style={{ padding: '1rem', verticalAlign: 'top' }}>
                      <div style={{ display: 'flex', gap: '0.5rem', flexDirection: 'column' }}>
                        <button
                          onClick={() => handleEditTrait(trait.id)}
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
                          onClick={() => handleToggleStatus(trait.id, trait.status)}
                          style={{
                            padding: '0.25rem 0.5rem',
                            fontSize: '0.75rem',
                            border: '1px solid #d1d5db',
                            borderRadius: '0.25rem',
                            backgroundColor: trait.status === 'active' ? '#fef3c7' : '#dcfce7',
                            color: trait.status === 'active' ? '#d97706' : '#166534',
                            cursor: 'pointer'
                          }}
                        >
                          {trait.status === 'active' ? 'Deactivate' : 'Activate'}
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
            {traitsData.filter(t => t.status === 'active').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Traits</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {traitsData.filter(t => t.status === 'draft').length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Draft Traits</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#dc2626', marginBottom: '0.5rem' }}>
            {traitsData.filter(t => t.status === 'inactive').length}
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

      {/* Edit Trait Modal */}
      {showEditModal && editingTrait && (
        <EditTraitModal
          trait={editingTrait}
          onSave={handleSaveEdit}
          onClose={handleCloseEditModal}
        />
      )}
    </div>
  );
};

// Edit Trait Modal Component
const EditTraitModal = ({ trait, onSave, onClose }) => {
  const [formData, setFormData] = useState({
    name: trait.name || '',
    category: trait.category || '',
    description: trait.description || ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (isSubmitting) return;
    
    // Validation
    if (!formData.name.trim()) {
      alert('Please enter a trait name');
      return;
    }
    if (!formData.category.trim()) {
      alert('Please enter a category');
      return;
    }
    if (!formData.description.trim()) {
      alert('Please enter a description');
      return;
    }

    setIsSubmitting(true);
    try {
      await onSave(formData);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000
    }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '0.5rem',
        padding: '2rem',
        maxWidth: '600px',
        width: '90%',
        maxHeight: '80vh',
        overflow: 'auto'
      }}>
        <h2 style={{ fontSize: '1.5rem', fontWeight: '600', marginBottom: '1.5rem' }}>
          Edit Trait
        </h2>
        
        <form onSubmit={handleSubmit}>
          {/* Trait Name */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Trait Name *
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleInputChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
              placeholder="Enter trait name"
            />
          </div>

          {/* Category */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Category *
            </label>
            <input
              type="text"
              name="category"
              value={formData.category}
              onChange={handleInputChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
              placeholder="Enter trait category"
            />
          </div>

          {/* Description */}
          <div style={{ marginBottom: '2rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Description *
            </label>
            <textarea
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              required
              rows={4}
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem',
                resize: 'vertical'
              }}
              placeholder="Describe the trait"
            />
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end' }}>
            <button
              type="button"
              onClick={onClose}
              style={{
                padding: '0.75rem 1.5rem',
                fontSize: '0.875rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                backgroundColor: 'white',
                color: '#374151',
                cursor: 'pointer'
              }}
              disabled={isSubmitting}
            >
              Cancel
            </button>
            <button
              type="submit"
              style={{
                padding: '0.75rem 1.5rem',
                fontSize: '0.875rem',
                border: 'none',
                borderRadius: '0.375rem',
                backgroundColor: '#d946ef',
                color: 'white',
                cursor: 'pointer',
                opacity: isSubmitting ? 0.6 : 1
              }}
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Saving...' : 'Save Changes'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default DomainTraits;
