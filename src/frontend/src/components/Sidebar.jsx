import { NavLink } from 'react-router-dom';
import { 
  HomeIcon, 
  ClipboardDocumentListIcon, 
  AcademicCapIcon 
} from '@heroicons/react/24/outline';

const Sidebar = () => {
  const navigation = [
    { name: 'Home', href: '/', icon: HomeIcon },
    { name: '360 Survey', href: '/survey', icon: ClipboardDocumentListIcon },
    { name: 'Learning Plans', href: '/learning-plans', icon: AcademicCapIcon },
  ];

  return (
    <div className="sidebar">
      {/* Logo/Brand */}
      <div className="sidebar-header">
        <h1 className="sidebar-title">360+AI Planner</h1>
      </div>

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
            <span className="user-avatar-text">U</span>
          </div>
          <div>
            <p className="user-name">User</p>
            <p className="user-email">user@example.com</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
