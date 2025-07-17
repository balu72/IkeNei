import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/Layout';
import Login from './components/Login';
import Home from './pages/Home';
import AssesseeHome from './pages/AssesseeHome';
import CoachHome from './pages/CoachHome';
import AdminHome from './pages/AdminHome';
import Survey from './pages/Survey';
import LearningPlans from './pages/LearningPlans';
import ProfileUpdate from './pages/ProfileUpdate';
import './App.css';

// Protected Route Component
const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();
  
  if (loading) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        background: 'linear-gradient(135deg, #fdf4ff 0%, #fae8ff 100%)'
      }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{
            width: '3rem',
            height: '3rem',
            border: '3px solid #d946ef',
            borderTop: '3px solid transparent',
            borderRadius: '50%',
            animation: 'spin 1s linear infinite',
            margin: '0 auto 1rem'
          }}></div>
          <p style={{ color: '#6b7280' }}>Loading...</p>
        </div>
      </div>
    );
  }
  
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};

// Role-based Home Component
const RoleBasedHome = () => {
  const { isAssessee, isCoach, isAdmin } = useAuth();
  
  if (isAssessee) return <AssesseeHome />;
  if (isCoach) return <CoachHome />;
  if (isAdmin) return <AdminHome />;
  
  // Fallback to generic home
  return <Home />;
};

// Main App Routes
const AppRoutes = () => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return (
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    );
  }

  return (
    <Routes>
      <Route path="/login" element={<Navigate to="/" replace />} />
      <Route path="/" element={<Layout />}>
        <Route index element={<RoleBasedHome />} />
        
        {/* Legacy routes for backward compatibility */}
        <Route path="survey" element={<Survey />} />
        <Route path="learning-plans" element={<LearningPlans />} />
        
        {/* Assessee Routes */}
        <Route path="my-surveys" element={<Survey />} />
        <Route path="my-learning-progress" element={<LearningPlans />} />
        <Route path="profile" element={<ProfileUpdate />} />
        
        {/* Coach Routes */}
        <Route path="assessees" element={<div>Assessees Management (Coming Soon)</div>} />
        <Route path="survey-management" element={<div>Survey Management (Coming Soon)</div>} />
        <Route path="coaching-tools" element={<div>Coaching Tools (Coming Soon)</div>} />
        <Route path="reports" element={<div>Reports (Coming Soon)</div>} />
        
        {/* Admin Routes */}
        <Route path="user-management" element={<div>User Management (Coming Soon)</div>} />
        <Route path="system-settings" element={<div>System Settings (Coming Soon)</div>} />
        <Route path="analytics" element={<div>Analytics (Coming Soon)</div>} />
        <Route path="form-templates" element={<div>Form Templates (Coming Soon)</div>} />
        
        {/* Catch all route */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <AppRoutes />
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
