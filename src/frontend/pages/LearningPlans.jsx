const LearningPlans = () => {
  return (
    <div style={{ maxWidth: '1024px', margin: '0 auto' }}>
      <div className="page-header">
        <h1 className="page-title">Learning Plans</h1>
        <p className="page-description">AI-powered personalized learning paths for your development</p>
      </div>
      
      <div className="card">
        <div className="card-center">
          <div className="card-icon">
            <span>🎯</span>
          </div>
          <h2 className="card-title">AI-Powered Learning Plans</h2>
          <p className="card-text">
            Get personalized learning recommendations based on your 360° feedback analysis. 
            Our AI creates tailored development paths to help you grow professionally.
          </p>
          <div className="button-group">
            <button className="btn-primary">
              Generate Learning Plan
            </button>
            <button className="btn-secondary">
              View Progress
            </button>
          </div>
        </div>
      </div>
      
      {/* Feature Preview Cards */}
      <div className="features-grid">
        <div className="card">
          <h3 className="feature-title">AI Analysis</h3>
          <p className="feature-description">
            Advanced AI processes your feedback to identify strengths and development areas
          </p>
        </div>
        
        <div className="card">
          <h3 className="feature-title">Personalized Paths</h3>
          <p className="feature-description">
            Custom learning journeys tailored to your specific needs and goals
          </p>
        </div>
        
        <div className="card">
          <h3 className="feature-title">Progress Tracking</h3>
          <p className="feature-description">
            Monitor your development progress and adjust plans as you grow
          </p>
        </div>
      </div>
      
      {/* Sample Learning Plan Preview */}
      <div style={{ 
        marginTop: '2rem', 
        background: 'linear-gradient(to right, #fae8ff, #fdf2f8)', 
        borderRadius: '0.5rem', 
        padding: '1.5rem', 
        border: '1px solid #f0abfc' 
      }}>
        <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#111827', marginBottom: '1rem' }}>
          Sample Learning Plan Structure
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <div style={{ 
              width: '0.5rem', 
              height: '0.5rem', 
              backgroundColor: '#d946ef', 
              borderRadius: '50%', 
              marginRight: '0.75rem' 
            }}></div>
            <span style={{ color: '#374151' }}>Leadership Communication Skills</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <div style={{ 
              width: '0.5rem', 
              height: '0.5rem', 
              backgroundColor: '#d946ef', 
              borderRadius: '50%', 
              marginRight: '0.75rem' 
            }}></div>
            <span style={{ color: '#374151' }}>Strategic Thinking Development</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <div style={{ 
              width: '0.5rem', 
              height: '0.5rem', 
              backgroundColor: '#d946ef', 
              borderRadius: '50%', 
              marginRight: '0.75rem' 
            }}></div>
            <span style={{ color: '#374151' }}>Team Management Techniques</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <div style={{ 
              width: '0.5rem', 
              height: '0.5rem', 
              backgroundColor: '#d946ef', 
              borderRadius: '50%', 
              marginRight: '0.75rem' 
            }}></div>
            <span style={{ color: '#374151' }}>Emotional Intelligence Enhancement</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LearningPlans;
