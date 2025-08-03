import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { surveysAPI, traitsAPI } from '../../services/api';

const CreateSurvey = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    surveyName: '',
    description: '',
    selectedTraits: [],
    targetSector: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  // API data state
  const [availableTraits, setAvailableTraits] = useState([]);
  const [targetSectors, setTargetSectors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch data from APIs
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Fetch traits and trait categories for sectors
        const [traitsRes, categoriesRes] = await Promise.all([
          traitsAPI.getAll({ status: 'active' }), // Get only active traits
          traitsAPI.getCategories() // Get trait categories which can serve as sectors
        ]);
        
        if (traitsRes.success) {
          setAvailableTraits(traitsRes.data || []);
        }
        
        if (categoriesRes.success) {
          setTargetSectors(categoriesRes.data || []);
        }
        
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err.message || 'Failed to load data');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleTraitSelection = (traitObj) => {
    const traitId = traitObj.id || traitObj._id;
    const traitName = traitObj.name;
    
    setFormData(prev => {
      const isSelected = prev.selectedTraits.some(t => t.id === traitId);
      if (isSelected) {
        return {
          ...prev,
          selectedTraits: prev.selectedTraits.filter(t => t.id !== traitId)
        };
      } else {
        return {
          ...prev,
          selectedTraits: [...prev.selectedTraits, { 
            id: traitId, 
            name: traitName, 
            weightage: 0 
          }]
        };
      }
    });
  };

  const handleWeightageChange = (traitId, weightage) => {
    setFormData(prev => ({
      ...prev,
      selectedTraits: prev.selectedTraits.map(trait =>
        trait.id === traitId ? { ...trait, weightage: parseInt(weightage) || 0 } : trait
      )
    }));
  };

  const getTotalWeightage = () => {
    return formData.selectedTraits.reduce((total, trait) => total + trait.weightage, 0);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (isSubmitting) return;
    
    // Validation
    if (!formData.surveyName.trim()) {
      alert('Please enter a survey name');
      return;
    }
    if (!formData.description.trim()) {
      alert('Please enter a description');
      return;
    }
    if (formData.selectedTraits.length === 0) {
      alert('Please select at least one trait');
      return;
    }
    if (!formData.targetSector) {
      alert('Please select a target sector');
      return;
    }
    
    const totalWeightage = getTotalWeightage();
    if (totalWeightage !== 100) {
      alert(`Total weightage must equal 100%. Current total: ${totalWeightage}%`);
      return;
    }

    setIsSubmitting(true);
    try {
      console.log('Creating survey with data:', formData);
      
      // Prepare data for API call
      const surveyData = {
        title: formData.surveyName,
        description: formData.description,
        traits: formData.selectedTraits,
        target_sector: formData.targetSector
      };
      
      const response = await surveysAPI.create(surveyData);
      
      if (response.success) {
        alert('Survey created successfully!');
        navigate('/');
      } else {
        alert('Failed to create survey: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error creating survey:', error);
      alert('Failed to create survey: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  // Loading state
  if (loading) {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Create New Survey</h1>
        <div style={{ padding: '2rem' }}>
          <p>Loading traits and categories...</p>
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
        <h1 className="page-title">Create New Survey</h1>
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
    <div style={{ maxWidth: '800px', margin: '0 auto' }}>
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
        <h1 className="page-title">Create New Survey</h1>
        <p className="page-description">
          Define a new survey/questionnaire with traits, weightages, and target sector.
        </p>
      </div>

      {/* Create Survey Form */}
      <div className="card">
        <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
          {/* Survey Name */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Survey Name *
            </label>
            <input
              type="text"
              name="surveyName"
              value={formData.surveyName}
              onChange={handleInputChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
              placeholder="Enter survey name"
            />
          </div>

          {/* Description */}
          <div style={{ marginBottom: '1.5rem' }}>
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
              placeholder="Enter survey description and purpose"
            />
          </div>

          {/* Traits Selection */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Select Traits *
            </label>
            <div style={{
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              padding: '1rem',
              maxHeight: '200px',
              overflow: 'auto',
              backgroundColor: '#fafafa'
            }}>
              {availableTraits.map((trait) => (
                <label key={trait.id || trait._id} style={{
                  display: 'flex',
                  alignItems: 'center',
                  marginBottom: '0.5rem',
                  cursor: 'pointer'
                }}>
                  <input
                    type="checkbox"
                    checked={formData.selectedTraits.some(t => t.id === (trait.id || trait._id))}
                    onChange={() => handleTraitSelection(trait)}
                    style={{ marginRight: '0.5rem' }}
                  />
                  <span style={{ fontSize: '0.875rem' }}>{trait.name}</span>
                </label>
              ))}
            </div>
          </div>

          {/* Weightage for Selected Traits */}
          {formData.selectedTraits.length > 0 && (
            <div style={{ marginBottom: '1.5rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                Weightage for Each Trait * (Total must equal 100%)
              </label>
              <div style={{
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                padding: '1rem',
                backgroundColor: '#f9fafb'
              }}>
                {formData.selectedTraits.map((trait) => (
                  <div key={trait.id} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    marginBottom: '0.75rem',
                    padding: '0.5rem',
                    backgroundColor: 'white',
                    borderRadius: '0.25rem',
                    border: '1px solid #e5e7eb'
                  }}>
                    <span style={{ fontSize: '0.875rem', fontWeight: '500' }}>{trait.name}</span>
                    <div style={{ display: 'flex', alignItems: 'center' }}>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={trait.weightage}
                        onChange={(e) => handleWeightageChange(trait.id, e.target.value)}
                        style={{
                          width: '80px',
                          padding: '0.5rem',
                          border: '1px solid #d1d5db',
                          borderRadius: '0.25rem',
                          fontSize: '0.875rem',
                          marginRight: '0.5rem'
                        }}
                      />
                      <span style={{ fontSize: '0.875rem', color: '#6b7280' }}>%</span>
                    </div>
                  </div>
                ))}
                <div style={{
                  marginTop: '1rem',
                  padding: '0.75rem',
                  backgroundColor: getTotalWeightage() === 100 ? '#dcfce7' : '#fef2f2',
                  border: `1px solid ${getTotalWeightage() === 100 ? '#bbf7d0' : '#fecaca'}`,
                  borderRadius: '0.375rem',
                  textAlign: 'center'
                }}>
                  <span style={{
                    fontSize: '0.875rem',
                    fontWeight: '600',
                    color: getTotalWeightage() === 100 ? '#166534' : '#dc2626'
                  }}>
                    Total Weightage: {getTotalWeightage()}%
                  </span>
                </div>
              </div>
            </div>
          )}

          {/* Target Sector */}
          <div style={{ marginBottom: '2rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Target Sector *
            </label>
            <select
              name="targetSector"
              value={formData.targetSector}
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
              <option value="">Select target sector</option>
              {targetSectors.map((sector) => (
                <option key={sector} value={sector}>{sector}</option>
              ))}
            </select>
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
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateSurvey;
