import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const CreateTrait = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    traitName: '',
    description: '',
    items: [
      {
        question: '',
        level: ''
      }
    ]
  });

  const levels = ['basic', 'medium', 'advanced'];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleItemChange = (index, field, value) => {
    setFormData(prev => ({
      ...prev,
      items: prev.items.map((item, i) => 
        i === index ? { ...item, [field]: value } : item
      )
    }));
  };

  const addItem = () => {
    setFormData(prev => ({
      ...prev,
      items: [...prev.items, { question: '', level: '' }]
    }));
  };

  const removeItem = (index) => {
    if (formData.items.length > 1) {
      setFormData(prev => ({
        ...prev,
        items: prev.items.filter((_, i) => i !== index)
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Validation
    if (!formData.traitName.trim()) {
      alert('Please enter a trait name');
      return;
    }
    if (!formData.description.trim()) {
      alert('Please enter a description');
      return;
    }
    
    // Validate items
    for (let i = 0; i < formData.items.length; i++) {
      const item = formData.items[i];
      if (!item.question.trim()) {
        alert(`Please enter a question for item ${i + 1}`);
        return;
      }
      if (!item.level) {
        alert(`Please select a level for item ${i + 1}`);
        return;
      }
    }

    console.log('Trait data:', formData);
    alert('Trait created successfully!');
    navigate('/');
  };

  const handleCancel = () => {
    navigate('/');
  };

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
        <h1 className="page-title">Create New Trait</h1>
        <p className="page-description">
          Define a new trait/competency with assessment questions and difficulty levels.
        </p>
      </div>

      {/* Create Trait Form */}
      <div className="card">
        <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
          {/* Trait Name */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
              Trait Name *
            </label>
            <input
              type="text"
              name="traitName"
              value={formData.traitName}
              onChange={handleInputChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '0.375rem',
                fontSize: '0.875rem'
              }}
              placeholder="Enter trait name (e.g., Strategic Thinking, Leadership)"
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
              placeholder="Describe what this trait measures and its importance"
            />
          </div>

          {/* Items Section */}
          <div style={{ marginBottom: '2rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <h3 style={{ fontSize: '1rem', fontWeight: '600', color: '#374151' }}>
                Assessment Items
              </h3>
              <button
                type="button"
                onClick={addItem}
                className="btn-secondary"
                style={{ fontSize: '0.75rem', padding: '0.5rem 1rem' }}
              >
                + Add Item
              </button>
            </div>

            {formData.items.map((item, index) => (
              <div key={index} style={{ 
                border: '1px solid #e5e7eb', 
                borderRadius: '0.5rem', 
                padding: '1.5rem', 
                marginBottom: '1rem',
                backgroundColor: index % 2 === 0 ? '#fafafa' : '#f0f9ff'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                  <h4 style={{ fontSize: '0.875rem', fontWeight: '600', color: '#374151' }}>
                    Item {index + 1}
                  </h4>
                  {formData.items.length > 1 && (
                    <button
                      type="button"
                      onClick={() => removeItem(index)}
                      style={{
                        background: 'none',
                        border: 'none',
                        color: '#dc2626',
                        cursor: 'pointer',
                        fontSize: '0.875rem'
                      }}
                    >
                      Remove
                    </button>
                  )}
                </div>

                {/* Question */}
                <div style={{ marginBottom: '1rem' }}>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                    Question *
                  </label>
                  <textarea
                    value={item.question}
                    onChange={(e) => handleItemChange(index, 'question', e.target.value)}
                    required
                    rows={3}
                    style={{
                      width: '100%',
                      padding: '0.75rem',
                      border: '1px solid #d1d5db',
                      borderRadius: '0.375rem',
                      fontSize: '0.875rem',
                      resize: 'vertical'
                    }}
                    placeholder="Enter the assessment question or statement"
                  />
                </div>

                {/* Level */}
                <div>
                  <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                    Level *
                  </label>
                  <select
                    value={item.level}
                    onChange={(e) => handleItemChange(index, 'level', e.target.value)}
                    required
                    style={{
                      width: '100%',
                      padding: '0.75rem',
                      border: '1px solid #d1d5db',
                      borderRadius: '0.375rem',
                      fontSize: '0.875rem'
                    }}
                  >
                    <option value="">Select difficulty level</option>
                    {levels.map((level) => (
                      <option key={level} value={level}>
                        {level.charAt(0).toUpperCase() + level.slice(1)}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
            ))}
          </div>

          {/* Summary */}
          <div style={{ 
            marginBottom: '2rem',
            padding: '1rem',
            backgroundColor: '#f0f9ff',
            border: '1px solid #bae6fd',
            borderRadius: '0.375rem'
          }}>
            <h4 style={{ fontSize: '0.875rem', fontWeight: '600', marginBottom: '0.5rem', color: '#0369a1' }}>
              Summary
            </h4>
            <p style={{ fontSize: '0.875rem', color: '#0369a1', marginBottom: '0.5rem' }}>
              <strong>Trait:</strong> {formData.traitName || 'Not specified'}
            </p>
            <p style={{ fontSize: '0.875rem', color: '#0369a1', marginBottom: '0.5rem' }}>
              <strong>Total Items:</strong> {formData.items.length}
            </p>
            <p style={{ fontSize: '0.875rem', color: '#0369a1' }}>
              <strong>Level Distribution:</strong> {
                levels.map(level => {
                  const count = formData.items.filter(item => item.level === level).length;
                  return count > 0 ? `${level.charAt(0).toUpperCase() + level.slice(1)}: ${count}` : null;
                }).filter(Boolean).join(', ') || 'None selected'
              }
            </p>
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
              Create Trait
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateTrait;
