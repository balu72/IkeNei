import { NavLink } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { 
  HomeIcon, 
  ClipboardDocumentListIcon, 
  AcademicCapIcon,
  UserGroupIcon,
  Cog6ToothIcon,
  ChartBarIcon,
  DocumentTextIcon,
  UserIcon,
  ArrowRightOnRectangleIcon
} from '@heroicons/react/24/outline';

const Sidebar = () => {
  const { user, logout, isAssessee, isCoach, isAdmin } = useAuth();

  // Role-based navigation
  const getNavigation = () => {
    if (isAssessee) {
      return [
        { name: 'Home', href: '/', icon: HomeIcon },
        { name: 'My Surveys', href: '/my-surveys', icon: ClipboardDocumentListIcon },
        { name: 'My Learning Plans', href: '/my-learning-plans', icon: AcademicCapIcon },
        { name: 'My Progress', href: '/my-progress', icon: ChartBarIcon },
        { name: 'Profile', href: '/profile', icon: UserIcon },
      ];
    }
    
    if (isCoach) {
      return [
        { name: 'Home', href: '/', icon: HomeIcon },
        { name: 'Assessees', href: '/assessees', icon: UserGroupIcon },
        { name: 'Survey Management', href: '/survey-management', icon: ClipboardDocumentListIcon },
        { name: 'Coaching Tools', href: '/coaching-tools', icon: AcademicCapIcon },
        { name: 'Reports', href: '/reports', icon: ChartBarIcon },
      ];
    }
    
    if (isAdmin) {
      return [
        { name: 'Home', href: '/', icon: HomeIcon },
        { name: 'User Management', href: '/user-management', icon: UserGroupIcon },
        { name: 'System Settings', href: '/system-settings', icon: Cog6ToothIcon },
        { name: 'Analytics', href: '/analytics', icon: ChartBarIcon },
        { name: 'Form Templates', href: '/form-templates', icon: DocumentTextIcon },
      ];
    }
    
    // Default navigation
    return [
      { name: 'Home', href: '/', icon: HomeIcon },
      { name: '360 Survey', href: '/survey', icon: ClipboardDocumentListIcon },
      { name: 'Learning Plans', href: '/learning-plans', icon: AcademicCapIcon },
    ];
  };

  const navigation = getNavigation();

  const getRoleDisplayName = () => {
    if (isAssessee) return 'Assessee';
    if (isCoach) return 'Coach';
    if (isAdmin) return 'Administrator';
    return 'User';
  };

  const getRoleColor = () => {
    if (isAssessee) return '#10b981'; // Green
    if (isCoach) return '#3b82f6';   // Blue
    if (isAdmin) return '#ef4444';   // Red
    return '#6b7280';                // Gray
  };

  return (
    <div className="sidebar">
      {/* Logo/Brand */}
      <div className="sidebar-header">
        <h1 className="sidebar-title">360+AI Planner</h1>
      </div>

      {/* User Role Badge */}
      {user && (
        <div style={{ 
          padding: '1rem', 
          borderBottom: '1px solid #e5e7eb',
          backgroundColor: '#fafafa'
        }}>
          <div style={{
            display: 'inline-block',
            backgroundColor: getRoleColor(),
            color: 'white',
            padding: '0.25rem 0.75rem',
            borderRadius: '1rem',
            fontSize: '0.75rem',
            fontWeight: '500',
            textTransform: 'uppercase',
            letterSpacing: '0.05em'
          }}>
            {getRoleDisplayName()}
          </div>
        </div>
      )}

      {/* Navigation */}
      <nav className="sidebar-nav">
        <div className="nav-items">
          {navigation.map((item) => (
            <NavLink
              key={item.name}
              to={item.href}
              className={({ isActive }) =>
                `nav-item ${isActive ? 'active' : ''}`
              }
            >
              <item.icon className="nav-icon" />
              {item.name}
            </NavLink>
          ))}
        </div>
      </nav>

      {/* User Section */}
      <div className="user-section">
        <div className="user-info">
          <div className="user-avatar">
            <span className="user-avatar-text">{user?.avatar || 'U'}</span>
          </div>
          <div style={{ flex: 1 }}>
            <p className="user-name">{user?.name || 'User'}</p>
            <p className="user-email">{user?.email || 'user@example.com'}</p>
          </div>
          <button
            onClick={logout}
            style={{
              background: 'none',
              border: 'none',
              cursor: 'pointer',
              padding: '0.25rem',
              color: '#6b7280',
              borderRadius: '0.25rem',
              transition: 'color 0.2s'
            }}
            onMouseEnter={(e) => e.target.style.color = '#dc2626'}
            onMouseLeave={(e) => e.target.style.color = '#6b7280'}
            title="Logout"
          >
            <ArrowRightOnRectangleIcon style={{ width: '1.25rem', height: '1.25rem' }} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
