import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Mock user data for development - replace with actual API calls later
  const mockUsers = {
    'account@example.com': {
      id: '1',
      email: 'account@example.com',
      name: 'John Doe',
      role: 'account',
      avatar: 'JD'
    },
    'domainadmin@example.com': {
      id: '2',
      email: 'domainadmin@example.com',
      name: 'Sarah Wilson',
      role: 'domain_admin',
      avatar: 'SW'
    },
    'systemadmin@example.com': {
      id: '3',
      email: 'systemadmin@example.com',
      name: 'Mike Johnson',
      role: 'system_admin',
      avatar: 'MJ'
    }
  };

  useEffect(() => {
    // Check for stored user session
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    // Mock authentication - replace with actual API call
    const mockUser = mockUsers[email];
    if (mockUser && password === 'password') {
      setUser(mockUser);
      localStorage.setItem('user', JSON.stringify(mockUser));
      return { success: true };
    }
    return { success: false, error: 'Invalid credentials' };
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('user');
  };

  const register = async (userData) => {
    // Mock registration - replace with actual API call
    const newUser = {
      id: Date.now().toString(),
      ...userData,
      avatar: userData.name.split(' ').map(n => n[0]).join('').toUpperCase()
    };
    setUser(newUser);
    localStorage.setItem('user', JSON.stringify(newUser));
    return { success: true };
  };

  const updateProfile = async (profileData) => {
    // Mock profile update - replace with actual API call
    const updatedUser = { ...user, ...profileData };
    setUser(updatedUser);
    localStorage.setItem('user', JSON.stringify(updatedUser));
    return { success: true };
  };

  const value = {
    user,
    login,
    logout,
    register,
    updateProfile,
    loading,
    isAuthenticated: !!user,
    isAccount: user?.role === 'account',
    isDomainAdmin: user?.role === 'domain_admin',
    isSystemAdmin: user?.role === 'system_admin'
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
