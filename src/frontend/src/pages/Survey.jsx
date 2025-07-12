const Survey = () => {
  return (
    <div style={{ maxWidth: '1024px', margin: '0 auto' }}>
      <div className="page-header">
        <h1 className="page-title">360° Survey</h1>
        <p className="page-description">Create and manage comprehensive feedback surveys</p>
      </div>
      
      <div className="card">
        <div className="card-center">
          <div className="card-icon">
            <span>📋</span>
          </div>
          <h2 className="card-title">360° Survey Module</h2>
          <p className="card-text">
            This section will allow you to create, distribute, and manage 360-degree feedback surveys 
            to gather comprehensive insights from peers, supervisors, and direct reports.
          </p>
          <div className="button-group">
            <button className="btn-primary">
              Create New Survey
            </button>
            <button className="btn-secondary">
              View Past Surveys
            </button>
          </div>
        </div>
      </div>
      
      {/* Feature Preview Cards */}
      <div className="features-grid">
        <div className="card">
          <h3 className="feature-title">Multi-Source Feedback</h3>
          <p className="feature-description">
            Collect feedback from supervisors, peers, direct reports, and self-assessments
          </p>
        </div>
        
        <div className="card">
          <h3 className="feature-title">Anonymous Options</h3>
          <p className="feature-description">
            Ensure honest feedback with anonymous submission capabilities
          </p>
        </div>
        
        <div className="card">
          <h3 className="feature-title">Real-time Tracking</h3>
          <p className="feature-description">
            Monitor survey progress and completion rates in real-time
          </p>
        </div>
      </div>
    </div>
  );
};

export default Survey;
