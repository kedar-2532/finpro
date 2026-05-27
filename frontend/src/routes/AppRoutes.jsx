import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from '../pages/auth/Login';
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import Transactions from "../pages/transactions/Transactions"
import Budgets from "../pages/budgets/Budgets";
import Analytics from "../pages/analytics/Analytics";
import Alerts from "../pages/alerts/Alerts";

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

                <Route path="/budgets" element={
                    <ProtectedRoute>
                        <Budgets />
                    </ProtectedRoute>
                } />

                <Route path="/analytics" element={
                    <ProtectedRoute>
                        <Analytics />
                    </ProtectedRoute>   
                } />

                <Route path="/alerts" element={
                    <ProtectedRoute>
                        <Alerts />
                    </ProtectedRoute>   
                } />
                
            </Routes>
        
        </BrowserRouter>
    );
}

export default AppRoutes;