import { useState } from "react";

import { AuthContext } from "./AuthContext";

function AuthProvider({ children }) {

  const [token, setToken] = useState(
    localStorage.getItem("access") || null
  );

  const login = (accessToken) => {
    localStorage.setItem("access", accessToken);

    setToken(accessToken);
  };

  const logout = () => {
    localStorage.removeItem("access");

    setToken(null);
  };

  return (
    <AuthContext.Provider
      value={{token,login,logout,}}>
      {children}
    </AuthContext.Provider>
  );
}

export default AuthProvider;