import { Link, useNavigate } from "react-router-dom";


function Sidebar() {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access');

        navigate('/login');
    };

  return (
    <div className='w-64 min-h-screen bg-blue-900 text-white p-5'>
        <h1 className='text-3xl font-bold mb-10'>
            FinPro
        </h1>
        <nav className='flex flex-col gap-4'>

            <Link to='/dashboard'>
                Dashboard
            </Link>
            
            <Link to='/transactions'>
                Transactions
            </Link>

            <Link to='/budgets'>
                Budgets
            </Link>

            <Link to='/analytics'>
                Analytics
            </Link>

            <button onClick={handleLogout} className='bg-red-500 mt-10 p-2 rounded-lg'>
                Logout
            </button>

        </nav>      
    </div>
  );
}

export default Sidebar;
