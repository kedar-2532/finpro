import { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Login() {

  const [formData, setFormData] = useState({
    email: "", 
    password: "",

  });

  const navigate = useNavigate();
  
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {

  e.preventDefault();

  try {

    const response = await fetch(
      "http://127.0.0.1:8000/api/auth/login/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      }
    );

    const data = await response.json();

    console.log('DATA:',data);

    console.log('STATUS:', response.status);

    if(response.ok) {

    localStorage.setItem("access", data.access);

    alert("Login Successful");

    navigate("/dashboard");

  } else {
    
    alert("Invalid Credentails");
  }

} catch (error) {

    console.log('FULL ERROR:',error);

    if (error.response){
      console.log('Response Data:', error.respnse.data);

      console.log('Response Status:', error.response.status);
    }

    alert("Login Failed");
  }
};

  return (
    <div className="min-h-screen flex items-center justify-center">

      <form onSubmit={handleSubmit}>

        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} />
        <br /><br />

        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} />

        <br /><br />

        <button type="submit">
          Login
        </button>

      </form>

    </div>
  );
}

export default Login;