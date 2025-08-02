import { useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import CreateSubjectModal from '../../components/CreateSubjectModal';
import CreateRespondantModal from '../../components/CreateRespondantModal';
import { subjectsAPI, respondentsAPI, surveysAPI } from '../../services/api';

const AccountHome = () => {
  const navigate = useNavigate();
  const [showSubjectModal, setShowSubjectModal] = useState(false);
  const [showRespondantModal, setShowRespondantModal] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [loading, setLoading] = useState(true);
  const [dashboardData, setDashboardData] = useState({
    subjects: [],
    respondents: [],
    surveys: [],
    stats: {
      subjectsCount: 0,
      respondentsCount: 0,
      liveSurveysCount: 0
    }
  });

  // Fetch dashboard data function
  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      
      // Fetch subjects, respondents, and surveys in parallel
      const [subjectsResponse, respondentsResponse, surveysResponse] = await Promise.all([
        subjectsAPI.getAll().catch(err => ({ success: false, error: err })),
        respondentsAPI.getAll().catch(err => ({ success: false, error: err })),
        surveysAPI.getMySurveys().catch(err => ({ success: false, error: err }))
      ]);

      console.log('📊 Surveys Response:', surveysResponse);

      const subjects = subjectsResponse.success ? subjectsResponse.data : [];
      const respondents = respondentsResponse.success ? respondentsResponse.data : [];
      const surveys = surveysResponse.success ? surveysResponse.data : [];

      console.log('📊 Surveys Count:', surveys.length);

      setDashboardData({
        subjects,
        respondents,
        surveys,
        stats: {
          subjectsCount: subjects.length,
          respondentsCount: respondents.length,
          liveSurveysCount: surveys.filter(s => s.status === 'active' || s.status === 'open').length
        }
      });

    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  // Fetch dashboard data on component mount
  useEffect(() => {
    fetchDashboardData();
  }, []);

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
      
      // Map form data to backend expected format
      const mappedData = {
        name: data.name,
        email: data.email,
        phone: data.phone,
        address: data.address,
        subject_id: data.subjectAttachedTo, // Map subjectAttachedTo to subject_id
        relationship: mapCategoryToRelationship(data.category), // Map category to relationship
        other_info: data.otherInfo
      };
      
      console.log('Mapped data for backend:', mappedData);
      const response = await respondentsAPI.create(mappedData);
      
      if (response.success) {
        alert('Respondent created successfully!');
        setShowRespondantModal(false);
        // Refresh dashboard data to show updated counts
        fetchDashboardData();
      } else {
        console.error('Backend validation error:', response.error);
        alert('Failed to create respondent: ' + (response.error?.message || 'Unknown error'));
      }
    } catch (error) {
      console.error('Error creating respondent:', error);
      console.error('Full error object:', error);
      alert('Failed to create respondent: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Helper function to map category to relationship
  const mapCategoryToRelationship = (category) => {
    // Only map "Others" to "other", keep all other categories as their original names
    if (category === 'Others') {
      return 'other';
    }
    return category;
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
            {loading ? '...' : dashboardData.stats.subjectsCount}
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
            {loading ? '...' : dashboardData.stats.respondentsCount}
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
            {loading ? '...' : dashboardData.stats.liveSurveysCount}
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
              {loading ? (
                <tr>
                  <td colSpan="5" style={{ padding: '2rem', textAlign: 'center', color: '#6b7280' }}>
                    Loading survey data...
                  </td>
                </tr>
              ) : dashboardData.subjects.length === 0 ? (
                <tr>
                  <td colSpan="5" style={{ padding: '2rem', textAlign: 'center', color: '#6b7280' }}>
                    No subjects found. Create a subject to get started.
                  </td>
                </tr>
              ) : (
                dashboardData.subjects.map((subject, index) => (
                  <tr key={subject.id || index} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151' }}>
                      {subject.name || 'Unknown Subject'}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151' }}>
                      {subject.respondents ? subject.respondents.join(', ') : 'No respondents assigned'}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151' }}>
                      {subject.survey_name || 'No survey assigned'}
                    </td>
                    <td style={{ padding: '1rem' }}>
                      <span style={{
                        backgroundColor: subject.status === 'active' ? '#dcfce7' : 
                                       subject.status === 'closed' ? '#fee2e2' : '#fef3c7',
                        color: subject.status === 'active' ? '#166534' : 
                               subject.status === 'closed' ? '#dc2626' : '#d97706',
                        padding: '0.25rem 0.75rem',
                        borderRadius: '1rem',
                        fontSize: '0.75rem',
                        fontWeight: '500'
                      }}>
                        {subject.status || 'Open'}
                      </span>
                    </td>
                    <td style={{ padding: '1rem' }}>
                      {subject.status === 'closed' ? (
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
                            console.log('View report for', subject.name);
                          }}
                        >
                          View Report
                        </a>
                      ) : (
                        <span style={{ color: '#6b7280' }}>-</span>
                      )}
                    </td>
                  </tr>
                ))
              )}
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
        subjects={dashboardData.subjects}
      />

    </div>
  );
};

export default AccountHome;
