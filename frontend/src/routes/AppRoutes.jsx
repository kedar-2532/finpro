import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from '../pages/auth/Login';
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import Transactions from "../pages/transactions/Transactions"


import ProtectedRoute from "./ProtectedRoute";

function AppRoutes() {
    return(
        <BrowserRouter>
            <Routes>

                <Route path="/login" element={<Login />} />
                
                <Route path="/register" element={<Register />} />
            
                <Route path="/dashboard" element={
                    <ProtectedRoute>
                        <Dashboard />
                    </ProtectedRoute>
                } />

                <Route path="/transactions" element={
                    <ProtectedRoute>
                        <Transactions />
                    </ProtectedRoute>
                } />
                
            </Routes>
        
        </BrowserRouter>
    );
}

export default AppRoutes;