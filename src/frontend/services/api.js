// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';

// API Response handler
const handleResponse = async (response) => {
  let data = null;
  
  // Check if response has content before parsing JSON
  const contentType = response.headers.get('content-type');
  if (contentType && contentType.includes('application/json')) {
    try {
      data = await response.json();
    } catch (error) {
      console.error('Failed to parse JSON response:', error);
      data = { error: { message: 'Invalid JSON response from server' } };
    }
  } else {
    // Handle non-JSON responses
    try {
      const text = await response.text();
      data = { message: text || 'No content' };
    } catch (error) {
      data = { error: { message: 'Failed to read response' } };
    }
  }
  
  if (!response.ok) {
    const errorMessage = data?.error?.message || 
                        data?.message || 
                        `HTTP error! status: ${response.status}`;
    throw new Error(errorMessage);
  }
  
  return data;
};

// Get auth token from localStorage
const getAuthToken = () => {
  return localStorage.getItem('token');
};

// API request wrapper with authentication
const apiRequest = async (endpoint, options = {}) => {
  const token = getAuthToken();
  
  const config = {
    headers: {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
      ...options.headers,
    },
    ...options,
  };

  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
    return handleResponse(response);
  } catch (error) {
    // Handle network errors
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      throw new Error('Network error: Unable to connect to server. Please check your internet connection.');
    }
    // Re-throw other errors (including those from handleResponse)
    throw error;
  }
};

// Authentication API
export const authAPI = {
  login: async (email, password) => {
    const response = await apiRequest('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    
    if (response.success && response.data.token) {
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
    }
    
    return response;
  },

  logout: async () => {
    try {
      await apiRequest('/auth/logout', { method: 'POST' });
    } finally {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
  },

  register: async (userData) => {
    return apiRequest('/auth/register', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  },

  getCurrentUser: async () => {
    return apiRequest('/auth/me');
  },

  updateProfile: async (profileData) => {
    return apiRequest('/auth/profile', {
      method: 'PUT',
      body: JSON.stringify(profileData),
    });
  },

  forgotPassword: async (email) => {
    return apiRequest('/auth/forgot', {
      method: 'POST',
      body: JSON.stringify({ email }),
    });
  },

  resetPassword: async (token, newPassword) => {
    return apiRequest('/auth/reset', {
      method: 'POST',
      body: JSON.stringify({ token, new_password: newPassword }),
    });
  },
};

// Accounts API (System Admin)
export const accountsAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/accounts${queryString ? `?${queryString}` : ''}`);
  },

  create: async (accountData) => {
    return apiRequest('/accounts', {
      method: 'POST',
      body: JSON.stringify(accountData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/accounts/${id}`);
  },

  update: async (id, accountData) => {
    return apiRequest(`/accounts/${id}`, {
      method: 'PUT',
      body: JSON.stringify(accountData),
    });
  },

  updateStatus: async (id, isActive) => {
    return apiRequest(`/accounts/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ is_active: isActive }),
    });
  },

  delete: async (id) => {
    return apiRequest(`/accounts/${id}`, { method: 'DELETE' });
  },
};

// Surveys API
export const surveysAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/surveys${queryString ? `?${queryString}` : ''}`);
  },

  create: async (surveyData) => {
    return apiRequest('/surveys', {
      method: 'POST',
      body: JSON.stringify(surveyData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/surveys/${id}`);
  },

  update: async (id, surveyData) => {
    return apiRequest(`/surveys/${id}`, {
      method: 'PUT',
      body: JSON.stringify(surveyData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/surveys/${id}`, { method: 'DELETE' });
  },

  updateStatus: async (id, status) => {
    return apiRequest(`/surveys/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status }),
    });
  },

  getAvailable: async () => {
    return apiRequest('/surveys/available');
  },

  getMySurveys: async () => {
    return apiRequest('/surveys/my-surveys');
  },

  submitResponses: async (id, responses) => {
    return apiRequest(`/surveys/${id}/responses`, {
      method: 'POST',
      body: JSON.stringify({ responses }),
    });
  },

  getResponses: async (id) => {
    return apiRequest(`/surveys/${id}/responses`);
  },

  runSurvey: async (id, data = {}) => {
    return apiRequest(`/surveys/${id}/run`, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },
};

// Traits API
export const traitsAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/traits${queryString ? `?${queryString}` : ''}`);
  },

  create: async (traitData) => {
    return apiRequest('/traits', {
      method: 'POST',
      body: JSON.stringify(traitData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/traits/${id}`);
  },

  update: async (id, traitData) => {
    return apiRequest(`/traits/${id}`, {
      method: 'PUT',
      body: JSON.stringify(traitData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/traits/${id}`, { method: 'DELETE' });
  },

  updateStatus: async (id, status) => {
    return apiRequest(`/traits/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status }),
    });
  },

  getCategories: async () => {
    return apiRequest('/traits/categories');
  },

  getUsage: async () => {
    return apiRequest('/traits/usage');
  },
};

// Subjects API
export const subjectsAPI = {
  getAll: async () => {
    return apiRequest('/subjects');
  },

  create: async (subjectData) => {
    return apiRequest('/subjects', {
      method: 'POST',
      body: JSON.stringify(subjectData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/subjects/${id}`);
  },

  update: async (id, subjectData) => {
    return apiRequest(`/subjects/${id}`, {
      method: 'PUT',
      body: JSON.stringify(subjectData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/subjects/${id}`, { method: 'DELETE' });
  },
};

// Respondents API
export const respondentsAPI = {
  getAll: async (subjectId = null) => {
    const params = subjectId ? `?subject_id=${subjectId}` : '';
    return apiRequest(`/respondents${params}`);
  },

  create: async (respondentData) => {
    return apiRequest('/respondents', {
      method: 'POST',
      body: JSON.stringify(respondentData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/respondents/${id}`);
  },

  update: async (id, respondentData) => {
    return apiRequest(`/respondents/${id}`, {
      method: 'PUT',
      body: JSON.stringify(respondentData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/respondents/${id}`, { method: 'DELETE' });
  },
};

// Reports API
export const reportsAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/reports${queryString ? `?${queryString}` : ''}`);
  },

  create: async (reportData) => {
    return apiRequest('/reports', {
      method: 'POST',
      body: JSON.stringify(reportData),
    });
  },

  getById: async (id) => {
    return apiRequest(`/reports/${id}`);
  },

  update: async (id, reportData) => {
    return apiRequest(`/reports/${id}`, {
      method: 'PUT',
      body: JSON.stringify(reportData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/reports/${id}`, { method: 'DELETE' });
  },

  generate: async (id, data = {}) => {
    return apiRequest(`/reports/${id}/generate`, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  getInstances: async (id, params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/reports/${id}/instances${queryString ? `?${queryString}` : ''}`);
  },

  updateStatus: async (id, status) => {
    return apiRequest(`/reports/${id}/status`, {
      method: 'PATCH',
      body: JSON.stringify({ status }),
    });
  },
};

// Dashboard API
export const dashboardAPI = {
  getStats: async () => {
    return apiRequest('/dashboard/stats');
  },

  getActivity: async () => {
    return apiRequest('/dashboard/activity');
  },

  getAnalytics: async () => {
    return apiRequest('/dashboard/analytics');
  },
};

// Settings API (System Admin)
export const settingsAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/settings${queryString ? `?${queryString}` : ''}`);
  },

  update: async (key, value) => {
    return apiRequest(`/settings/${key}`, {
      method: 'PUT',
      body: JSON.stringify({ value }),
    });
  },

  toggle: async (key) => {
    return apiRequest(`/settings/${key}/toggle`, { method: 'PATCH' });
  },

  reset: async (key) => {
    return apiRequest(`/settings/reset/${key}`, { method: 'POST' });
  },

  getCategories: async () => {
    return apiRequest('/settings/categories');
  },
};

// Billing API
export const billingAPI = {
  getAll: async (params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/billing${queryString ? `?${queryString}` : ''}`);
  },

  getById: async (id) => {
    return apiRequest(`/billing/${id}`);
  },

  getByAccount: async (accountId, params = {}) => {
    const queryString = new URLSearchParams(params).toString();
    return apiRequest(`/billing/account/${accountId}${queryString ? `?${queryString}` : ''}`);
  },

  getSummary: async () => {
    return apiRequest('/billing/summary');
  },

  calculate: async (subjectsCount, respondentsCount) => {
    return apiRequest('/billing/calculate', {
      method: 'POST',
      body: JSON.stringify({ subjects_count: subjectsCount, respondents_count: respondentsCount }),
    });
  },
};

// Notifications API
export const notificationsAPI = {
  getAll: async () => {
    return apiRequest('/notifications');
  },

  markAsRead: async (id) => {
    return apiRequest(`/notifications/${id}/read`, { method: 'PATCH' });
  },

  create: async (notificationData) => {
    return apiRequest('/notifications', {
      method: 'POST',
      body: JSON.stringify(notificationData),
    });
  },

  delete: async (id) => {
    return apiRequest(`/notifications/${id}`, { method: 'DELETE' });
  },
};

// Files API
export const filesAPI = {
  upload: async (file, type = 'document') => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('type', type);

    const token = getAuthToken();
    const response = await fetch(`${API_BASE_URL}/upload`, {
      method: 'POST',
      headers: {
        ...(token && { Authorization: `Bearer ${token}` }),
      },
      body: formData,
    });

    return handleResponse(response);
  },

  download: async (id) => {
    return apiRequest(`/files/${id}`);
  },

  delete: async (id) => {
    return apiRequest(`/files/${id}`, { method: 'DELETE' });
  },
};

// Analytics API
export const analyticsAPI = {
  getOverview: async () => {
    return apiRequest('/analytics/overview');
  },

  getSurveyAnalytics: async (surveyId = null) => {
    const endpoint = surveyId ? `/analytics/surveys/${surveyId}` : '/analytics/surveys';
    return apiRequest(endpoint);
  },

  getAccountAnalytics: async (accountId = null) => {
    const endpoint = accountId ? `/analytics/accounts/${accountId}` : '/analytics/accounts';
    return apiRequest(endpoint);
  },

  getSystemAnalytics: async () => {
    return apiRequest('/analytics/system');
  },
};

// Categories API
export const categoriesAPI = {
  getRespondentCategories: async () => {
    return apiRequest('/categories/respondent-categories');
  },
};
