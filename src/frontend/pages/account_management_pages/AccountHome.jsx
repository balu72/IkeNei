import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import CreateSubjectModal from '../../components/CreateSubjectModal';
import CreateRespondantModal from '../../components/CreateRespondantModal';
import { subjectsAPI, respondentsAPI, surveysAPI } from '../../services/api';

const AccountHome = () => {
  const navigate = useNavigate();
  const [showSubjectModal, setShowSubjectModal] = useState(false);
  const [showRespondantModal, setShowRespondantModal] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleUpdateProfile = () => {
    navigate('/profile');
  };

  const handleCreateSubject = () => {
    setShowSubjectModal(true);
  };

  const handleCreateRespondant = () => {
    setShowRespondantModal(true);
  };


  const handleRunSurvey = async () => {
    console.log('🚀 RUN SURVEY BUTTON CLICKED!');
    try {
      // First, get available surveys
      console.log('📡 Getting available surveys...');
      const availableSurveysResponse = await surveysAPI.getAvailable();
      console.log('📊 Available Surveys Response:', availableSurveysResponse);
      
      if (availableSurveysResponse.success && availableSurveysResponse.data && availableSurveysResponse.data.length > 0) {
        const surveys = availableSurveysResponse.data;
        console.log('✅ Found surveys:', surveys);
        
        // For now, let's auto-select the first survey or let user choose
        let selectedSurvey;
        if (surveys.length === 1) {
          selectedSurvey = surveys[0];
          console.log('🎯 Auto-selecting single survey:', selectedSurvey.title);
        } else {
          // Multiple surveys - let user choose (for now, just pick the first one)
          selectedSurvey = surveys[0];
          console.log('🎯 Multiple surveys found, selecting first:', selectedSurvey.title);
        }
        
        // Now actually run/initiate the survey
        console.log('🚀 Initiating survey run for survey ID:', selectedSurvey.id);
        const runSurveyResponse = await surveysAPI.runSurvey(selectedSurvey.id, {
          // Add any additional data needed for running the survey
          initiated_by: 'account_user',
          timestamp: new Date().toISOString()
        });
        
        console.log('📊 Run Survey Response:', runSurveyResponse);
        
        if (runSurveyResponse.success) {
          console.log('✅ Survey initiated successfully!');
          alert(`Survey "${selectedSurvey.title}" has been initiated successfully!`);
          // Navigate to the run survey page to show progress/details
          navigate('/run-survey');
        } else {
          console.log('❌ Failed to initiate survey');
          alert('Failed to initiate survey: ' + (runSurveyResponse.error?.message || 'Unknown error'));
        }
      } else {
        console.log('❌ No surveys available');
        alert('No surveys available to run at this time.');
      }
    } catch (error) {
      console.error('💥 Error running survey:', error);
      console.error('💥 Error details:', error.message, error.stack);
      alert('Error occurred while running survey: ' + error.message);
    }
  };

  const handleSubjectSubmit = async (data) => {
    if (isSubmitting) return;
    
    setIsSubmitting(true);
    try {
      console.log('Creating subject with data:', data);
      const response = await subjectsAPI.create(data);
      
      if (response.success) {
        alert('Subject created successfully!');
        setShowSubjectModal(false);
        // Optionally refresh the page or update the subjects list
      } else {
        alert('Failed to create subject: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error creating subject:', error);
      alert('Failed to create subject: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleRespondantSubmit = async (data) => {
    if (isSubmitting) return;
    
    setIsSubmitting(true);
    try {
      console.log('Creating respondent with data:', data);
      const response = await respondentsAPI.create(data);
      
      if (response.success) {
        alert('Respondent created successfully!');
        setShowRespondantModal(false);
        // Optionally refresh the page or update the respondents list
      } else {
        alert('Failed to create respondent: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error creating respondent:', error);
      alert('Failed to create respondent: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };


  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Welcome Section */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 className="page-title">Account Management Dashboard</h1>
        <p className="page-description">
          Manage your account settings, participate in surveys, and track your feedback responses.
        </p>
      </div>

      {/* Quick Stats */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#d946ef',
            marginBottom: '0.5rem'
          }}>
            2
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Subjects
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Taking 360 degree survey.
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#10b981',
            marginBottom: '0.5rem'
          }}>
            3
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Respondants
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Participating in surveys
          </p>
        </div>

        <div className="card" style={{ textAlign: 'center', padding: '1.5rem' }}>
          <div style={{ 
            fontSize: '2rem', 
            fontWeight: 'bold', 
            color: '#3b82f6',
            marginBottom: '0.5rem'
          }}>
            2
          </div>
          <h3 style={{ fontSize: '1rem', fontWeight: '600', marginBottom: '0.25rem' }}>
            Live Surveys
          </h3>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>
            Data Collection in Progress
          </p>
        </div>
      </div>

      {/* Action Buttons */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '2rem'
      }}>
        <button 
          className="btn-primary" 
          onClick={handleCreateSubject}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Subject
        </button>
        <button 
          className="btn-primary" 
          onClick={handleCreateRespondant}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Create New Respondant
        </button>
        <button 
          className="btn-primary" 
          onClick={handleRunSurvey}
          style={{ 
            width: '100%', 
            textAlign: 'center',
            padding: '1rem',
            fontSize: '0.875rem',
            fontWeight: '600'
          }}
        >
          Run Survey
        </button>
      </div>

      {/* Survey Table */}
      <div>
        <h2 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '1rem' }}>
          Survey Overview
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
                  color: '#374151'
                }}>
                  Subject
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Respondant
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Survey Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Status
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  View Report
                </th>
              </tr>
            </thead>
            <tbody>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>John Doe</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Sarah Wilson, Mike Johnson, Emily Davis
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Leadership Skills Assessment</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>Jane Smith</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Robert Brown, Lisa Anderson, David Wilson, Tom Harris
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Communication Skills Survey</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#fef3c7',
                    color: '#d97706',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
              <tr style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={{ padding: '1rem', color: '#374151' }}>Robert Brown</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  Emily Davis, Sarah Wilson, John Doe
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Team Management Review</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#fee2e2',
                    color: '#dc2626',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Closed
                  </span>
                </td>
                <td style={{ padding: '1rem' }}>
                  <a 
                    href="#" 
                    style={{
                      color: '#3b82f6',
                      textDecoration: 'underline',
                      fontSize: '0.875rem',
                      fontWeight: '500'
                    }}
                    onClick={(e) => {
                      e.preventDefault();
                      // Handle report view
                      console.log('View report for Team Management Review');
                    }}
                  >
                    View Report
                  </a>
                </td>
              </tr>
              <tr>
                <td style={{ padding: '1rem', color: '#374151' }}>Lisa Anderson</td>
                <td style={{ padding: '1rem', color: '#374151' }}>
                  David Wilson, Mike Johnson, Jane Smith, Robert Brown, Sarah Wilson
                </td>
                <td style={{ padding: '1rem', color: '#374151' }}>Project Management Skills</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{
                    backgroundColor: '#dcfce7',
                    color: '#166534',
                    padding: '0.25rem 0.75rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: '500'
                  }}>
                    Open
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>
                  -
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal Components */}
      <CreateSubjectModal
        isOpen={showSubjectModal}
        onClose={() => setShowSubjectModal(false)}
        onSubmit={handleSubjectSubmit}
      />

      <CreateRespondantModal
        isOpen={showRespondantModal}
        onClose={() => setShowRespondantModal(false)}
        onSubmit={handleRespondantSubmit}
      />

    </div>
  );
};

export default AccountHome;
