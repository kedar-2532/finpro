import { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../../services/AuthService';
import { AuthContext } from '../../context/AuthContext';


function Login() {
  const navigate = useNavigate();

  const { login } = useContext(AuthContext);

  const [formData, setformData] = useState({
    email: '',
    password: '',
  });

  const handelChange = (e) => {
    setformData({
      ...FormData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefualt();

    console.log('FORM SUBMITTED');

    try {
      console.log('Sending Request');

      const response = await loginUser(formData);

      login(response.access);

      alert('Login Successful');

      navigate('/dashboard');

    } catch (error) {

      console.log('ERROR:', error);

      console.log('ERROR RESPONSE:',error.response);

      alert('Invalid Credentials');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <form onSubmit={handleSubmit} className='bg-white p-8 rounded-xl shadow-lg w-96'>
        
        <h2 className='text-3xl font-bold mb-6 text-center'>FinPro Login</h2>

        <input type="text" name='email' placeholder='Email' className='w-full border p-3 rounded-b-lg' onChange={handelChange} />

        <input type="password" name='password' placeholder='Password' className='w-full border p-3 mb-4 rounded-lg' onChange={handelChange} />

        <button type='submit' className='w-full bg-blue-600 text-white p-3 rounded-lg'>Login</button>

      </form>

    </div>
  );
}

export default Login;