import { createContext, useState } from 'react';

export const AuthContext = createContext();

function AuthProvider({ childern }) {
  const [token, setToken] = useState(
    localStorage.getItem('access')
  );

  const login = (accessToken) => {
    localStorage.setItem('access', accessToken);
    setToken(accessToken);
  };

  const logout = () => {
    localStorage.removeItem('access');
    setToken(null);
  };

  return(
    <AuthContext.Provider value={{token,login,logout}}>
        {childern}
    </AuthContext.Provider>
  );
}

export default AuthProvider;
