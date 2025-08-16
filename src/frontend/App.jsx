import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/Layout';
import Login from './components/Login';
import Home from './pages/Home';
import AccountHome from './pages/account_management_pages/AccountHome';
import ProfileUpdate from './pages/account_management_pages/ProfileUpdate';
import Survey from './pages/account_management_pages/Survey';
import RunSurvey from './pages/account_management_pages/RunSurvey';
import DomainAdminHome from './pages/domain_admin_pages/DomainAdminHome';
import CreateSurvey from './pages/domain_admin_pages/CreateSurvey';
import CreateTrait from './pages/domain_admin_pages/CreateTrait';
import DefineReport from './pages/domain_admin_pages/DefineReport';
import DomainSurveys from './pages/domain_admin_pages/DomainSurveys';
import DomainTraits from './pages/domain_admin_pages/DomainTraits';
import DomainReports from './pages/domain_admin_pages/DomainReports';
import SysAdminHome from './pages/sys_admin_pages/SysAdminHome';
import CreateAccount from './pages/sys_admin_pages/CreateAccount';
import Accounts from './pages/sys_admin_pages/Accounts';
import EditAccount from './pages/sys_admin_pages/EditAccount';
import Surveys from './pages/sys_admin_pages/Surveys';
import SurveyDetails from './pages/sys_admin_pages/SurveyDetails';
import Settings from './pages/sys_admin_pages/Settings';
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
  const { isAccount, isDomainAdmin, isSystemAdmin } = useAuth();
  
  if (isAccount) return <AccountHome />;
  if (isDomainAdmin) return <DomainAdminHome />;
  if (isSystemAdmin) return <SysAdminHome />;
  
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
        
        {/* Account Routes */}
        <Route path="profile" element={<ProfileUpdate />} />
        <Route path="run-survey" element={<RunSurvey />} />
        
        {/* Domain Admin Routes */}
        <Route path="create-survey" element={<CreateSurvey />} />
        <Route path="create-trait" element={<CreateTrait />} />
        <Route path="create-account" element={<CreateAccount />} />
        <Route path="reports" element={<DefineReport />} />
        <Route path="domain-surveys" element={<DomainSurveys />} />
        <Route path="domain-traits" element={<DomainTraits />} />
        <Route path="domain-reports" element={<DomainReports />} />
        
        {/* System Admin Routes */}
        <Route path="account-management" element={<Accounts />} />
        <Route path="edit-account/:accountId" element={<EditAccount />} />
        <Route path="system-settings" element={<Settings />} />
        <Route path="analytics" element={<Surveys />} />
        <Route path="survey-details/:surveyId" element={<SurveyDetails />} />
        
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
