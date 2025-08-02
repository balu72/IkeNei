import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { accountsAPI } from '../../services/api';

const Accounts = () => {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterState, setFilterState] = useState('all');
  const [accountsData, setAccountsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch accounts data from API
  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        setLoading(true);
        const response = await accountsAPI.getAll();
        if (response.success) {
          setAccountsData(response.data || []);
        } else {
          setError('Failed to fetch accounts');
        }
      } catch (err) {
        setError(err.message || 'Failed to fetch accounts');
      } finally {
        setLoading(false);
      }
    };

    fetchAccounts();
  }, []);

  // Filter accounts based on search term and state filter
  const filteredAccounts = accountsData.filter(account => {
    const matchesSearch = account.account_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         account.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         account.account_type.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesState = filterState === 'all' || 
                        (filterState === 'active' && account.is_active) ||
                        (filterState === 'passive' && !account.is_active);
    
    return matchesSearch && matchesState;
  });

  const handleCreateAccount = () => {
    navigate('/create-account');
  };

  const handleBack = () => {
    navigate('/');
  };

  const getStateStyle = (state) => {
    return {
      backgroundColor: state === 'Active' ? '#dcfce7' : '#fef3c7',
      color: state === 'Active' ? '#166534' : '#d97706',
      padding: '0.25rem 0.75rem',
      borderRadius: '1rem',
      fontSize: '0.75rem',
      fontWeight: '500'
    };
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <button 
          onClick={handleBack}
          style={{
            background: 'none',
            border: 'none',
            color: '#d946ef',
            fontSize: '0.875rem',
            cursor: 'pointer',
            marginBottom: '1rem',
            display: 'flex',
            alignItems: 'center'
          }}
        >
          ← Back to Dashboard
        </button>
        <h1 className="page-title">Account Management</h1>
        <p className="page-description">
          View and manage global accounts, monitor account status, and perform administrative actions.
        </p>
      </div>

      {/* Controls */}
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        marginBottom: '2rem',
        gap: '1rem',
        flexWrap: 'wrap'
      }}>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', flex: 1 }}>
          {/* Search */}
          <input
            type="text"
            placeholder="Search accounts..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem',
              minWidth: '250px'
            }}
          />
          
          {/* State Filter */}
          <select
            value={filterState}
            onChange={(e) => setFilterState(e.target.value)}
            style={{
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '0.375rem',
              fontSize: '0.875rem'
            }}
          >
            <option value="all">All States</option>
            <option value="active">Active</option>
            <option value="passive">Passive</option>
          </select>
        </div>

        {/* Create Account Button */}
        <button
          onClick={handleCreateAccount}
          className="btn-primary"
          style={{ fontSize: '0.875rem' }}
        >
          Create New Account
        </button>
      </div>

      {/* Error Message */}
      {error && (
        <div className="card" style={{ padding: '1rem', marginBottom: '2rem', backgroundColor: '#fee2e2', border: '1px solid #fecaca' }}>
          <p style={{ color: '#dc2626', fontSize: '0.875rem' }}>
            Error: {error}
          </p>
        </div>
      )}

      {/* Accounts Table */}
      <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          padding: '1.5rem',
          borderBottom: '1px solid #e5e7eb'
        }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#374151' }}>
            All Accounts ({loading ? '...' : filteredAccounts.length})
          </h2>
        </div>

        <div style={{ overflow: 'auto' }}>
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
                  Account Name
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Contact Info
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Account Type
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  State
                </th>
                <th style={{ 
                  padding: '1rem', 
                  textAlign: 'left', 
                  fontWeight: '600',
                  color: '#374151'
                }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {filteredAccounts.length > 0 ? (
                filteredAccounts.map((account) => (
                  <tr key={account.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                    <td style={{ padding: '1rem', color: '#374151', fontWeight: '500' }}>
                      {account.account_name}
                    </td>
                    <td style={{ padding: '1rem', color: '#6b7280' }}>
                      {account.email}
                    </td>
                    <td style={{ padding: '1rem', color: '#374151' }}>
                      {account.account_type}
                    </td>
                    <td style={{ padding: '1rem' }}>
                      <span style={getStateStyle(account.is_active ? 'Active' : 'Passive')}>
                        {account.is_active ? 'Active' : 'Passive'}
                      </span>
                    </td>
                    <td style={{ padding: '1rem' }}>
                      <div style={{ display: 'flex', gap: '0.5rem' }}>
                        <button
                          onClick={() => console.log('Edit account:', account.id)}
                          style={{
                            padding: '0.25rem 0.5rem',
                            fontSize: '0.75rem',
                            border: '1px solid #d1d5db',
                            borderRadius: '0.25rem',
                            backgroundColor: 'white',
                            color: '#374151',
                            cursor: 'pointer'
                          }}
                        >
                          Edit
                        </button>
                        <button
                          onClick={() => console.log('Toggle state:', account.id)}
                          style={{
                            padding: '0.25rem 0.5rem',
                            fontSize: '0.75rem',
                            border: '1px solid #d1d5db',
                            borderRadius: '0.25rem',
                            backgroundColor: account.is_active ? '#fef3c7' : '#dcfce7',
                            color: account.is_active ? '#d97706' : '#166534',
                            cursor: 'pointer'
                          }}
                        >
                          {account.is_active ? 'Deactivate' : 'Activate'}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" style={{ 
                    padding: '2rem', 
                    textAlign: 'center', 
                    color: '#6b7280',
                    fontStyle: 'italic'
                  }}>
                    No accounts found matching your criteria.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Summary Stats */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1rem',
        marginTop: '2rem'
      }}>
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#10b981', marginBottom: '0.5rem' }}>
            {accountsData.filter(a => a.is_active === true).length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Active Accounts</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b', marginBottom: '0.5rem' }}>
            {accountsData.filter(a => a.is_active === false).length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Passive Accounts</p>
        </div>
        
        <div className="card" style={{ textAlign: 'center', padding: '1rem' }}>
          <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#3b82f6', marginBottom: '0.5rem' }}>
            {accountsData.length}
          </div>
          <p style={{ fontSize: '0.875rem', color: '#6b7280' }}>Total Accounts</p>
        </div>
      </div>
    </div>
  );
};

export default Accounts;
