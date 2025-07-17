import { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';

const ProfileUpdate = () => {
  const { user, updateProfile } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    grade: '',
    schoolName: '',
    studentId: '',
    dateOfBirth: '',
    parentContact: '',
    interests: '',
    academicGoals: ''
  });

  useEffect(() => {
    if (user) {
      setFormData({
        name: user.name || '',
        email: user.email || '',
        phone: user.phone || '',
        grade: user.grade || '',
        schoolName: user.schoolName || '',
        studentId: user.studentId || '',
        dateOfBirth: user.dateOfBirth || '',
        parentContact: user.parentContact || '',
        interests: user.interests || '',
        academicGoals: user.academicGoals || ''
      });
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const validateForm = () => {
    const errors = [];
    
    if (!formData.name.trim()) errors.push('Full name is required');
    if (formData.name.trim().length < 2) errors.push('Name must be at least 2 characters');
    if (!formData.grade) errors.push('Grade/Year is required');
    if (!formData.schoolName.trim()) errors.push('School name is required');
    if (!formData.dateOfBirth) errors.push('Date of birth is required');
    if (!formData.parentContact.trim()) errors.push('Parent/Guardian contact is required');
    
    // Validate date of birth (should be reasonable for high school)
    if (formData.dateOfBirth) {
      const birthDate = new Date(formData.dateOfBirth);
      const today = new Date();
      const age = today.getFullYear() - birthDate.getFullYear();
      if (age < 13 || age > 20) {
        errors.push('Please enter a valid date of birth for a high school student');
      }
    }
    
    // Validate phone format if provided
    if (formData.phone && !/^\+?[\d\s\-\(\)]+$/.test(formData.phone)) {
      errors.push('Please enter a valid phone number');
    }
    
    return errors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage('');
    
    const errors = validateForm();
    if (errors.length > 0) {
      setMessage(errors.join('. '));
      setLoading(false);
      return;
    }
    
    try {
      // Simulate API call delay
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Update user profile (this will be replaced with actual API call later)
      const updatedUser = { ...user, ...formData };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      
      setMessage('Profile updated successfully!');
      setTimeout(() => {
        navigate('/');
      }, 1500);
    } catch (error) {
      setMessage('Failed to update profile. Please try again.');
    } finally {
      setLoading(false);
    }
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
        <h1 className="page-title">Update Your Profile</h1>
        <p className="page-description">
          Keep your information up to date to get the best feedback and learning recommendations.
        </p>
      </div>

      {/* Profile Form */}
      <div className="card">
        <form onSubmit={handleSubmit} style={{ padding: '2rem' }}>
          {/* Personal Information Section */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              Personal Information
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Full Name *
                </label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                  placeholder="Enter your full name"
                />
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Email Address
                </label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  disabled
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem',
                    backgroundColor: '#f9fafb',
                    color: '#6b7280'
                  }}
                />
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Phone Number
                </label>
                <input
                  type="tel"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                  placeholder="Your phone number (optional)"
                />
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Date of Birth *
                </label>
                <input
                  type="date"
                  name="dateOfBirth"
                  value={formData.dateOfBirth}
                  onChange={handleChange}
                  required
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

          {/* School Information Section */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              School Information
            </h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Grade/Year *
                </label>
                <select
                  name="grade"
                  value={formData.grade}
                  onChange={handleChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                >
                  <option value="">Select your grade</option>
                  <option value="9th">9th Grade</option>
                  <option value="10th">10th Grade</option>
                  <option value="11th">11th Grade</option>
                  <option value="12th">12th Grade</option>
                </select>
              </div>
              
              <div>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                  Student ID
                </label>
                <input
                  type="text"
                  name="studentId"
                  value={formData.studentId}
                  onChange={handleChange}
                  style={{
                    width: '100%',
                    padding: '0.75rem',
                    border: '1px solid #d1d5db',
                    borderRadius: '0.375rem',
                    fontSize: '0.875rem'
                  }}
                  placeholder="Your student ID (optional)"
                />
              </div>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                School Name *
              </label>
              <input
                type="text"
                name="schoolName"
                value={formData.schoolName}
                onChange={handleChange}
                required
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  fontSize: '0.875rem'
                }}
                placeholder="Enter your school name"
              />
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                Parent/Guardian Contact *
              </label>
              <input
                type="text"
                name="parentContact"
                value={formData.parentContact}
                onChange={handleChange}
                required
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  fontSize: '0.875rem'
                }}
                placeholder="Parent/Guardian name and phone number"
              />
            </div>
          </div>

          {/* Additional Information Section */}
          <div style={{ marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem', color: '#374151' }}>
              About You
            </h2>
            
            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                Interests & Hobbies
              </label>
              <textarea
                name="interests"
                value={formData.interests}
                onChange={handleChange}
                rows={3}
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  fontSize: '0.875rem',
                  resize: 'vertical'
                }}
                placeholder="Tell us about your interests, hobbies, and activities you enjoy..."
                maxLength={500}
              />
              <p style={{ fontSize: '0.75rem', color: '#6b7280', marginTop: '0.25rem' }}>
                {formData.interests.length}/500 characters
              </p>
            </div>

            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: '500', color: '#374151', marginBottom: '0.5rem' }}>
                Academic Goals
              </label>
              <textarea
                name="academicGoals"
                value={formData.academicGoals}
                onChange={handleChange}
                rows={3}
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  border: '1px solid #d1d5db',
                  borderRadius: '0.375rem',
                  fontSize: '0.875rem',
                  resize: 'vertical'
                }}
                placeholder="What are your academic goals and future aspirations?"
                maxLength={500}
              />
              <p style={{ fontSize: '0.75rem', color: '#6b7280', marginTop: '0.25rem' }}>
                {formData.academicGoals.length}/500 characters
              </p>
            </div>
          </div>

          {/* Message Display */}
          {message && (
            <div style={{
              padding: '0.75rem',
              borderRadius: '0.375rem',
              marginBottom: '1rem',
              backgroundColor: message.includes('success') ? '#dcfce7' : '#fef2f2',
              border: `1px solid ${message.includes('success') ? '#bbf7d0' : '#fecaca'}`,
              color: message.includes('success') ? '#166534' : '#dc2626'
            }}>
              {message}
            </div>
          )}

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end' }}>
            <button
              type="button"
              onClick={handleCancel}
              className="btn-secondary"
              disabled={loading}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
              disabled={loading}
            >
              {loading ? 'Saving...' : 'Save Profile'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ProfileUpdate;
