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
    'assessee@example.com': {
      id: '1',
      email: 'assessee@example.com',
      name: 'John Doe',
      role: 'assessee',
      avatar: 'JD'
    },
    'coach@example.com': {
      id: '2',
      email: 'coach@example.com',
      name: 'Sarah Wilson',
      role: 'coach',
      avatar: 'SW'
    },
    'admin@example.com': {
      id: '3',
      email: 'admin@example.com',
      name: 'Mike Johnson',
      role: 'admin',
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

  const value = {
    user,
    login,
    logout,
    register,
    loading,
    isAuthenticated: !!user,
    isAssessee: user?.role === 'assessee',
    isCoach: user?.role === 'coach',
    isAdmin: user?.role === 'admin'
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
