import React, { useState } from 'react'; // Ensure React is in scope for JSX
import '../login_button/login_button.css'; // Correct relative import path for your CSS
import { useNavigate } from 'react-router-dom'; // Import useNavigate for React Router v6

function LoginButton() {
  const [click, setClick] = useState(false); // State to track button click
  const navigate = useNavigate(); // Hook to navigate between pages

  // Handle button click
  const handleClick = () => {
    setClick(true); // Change the state to true after clicking
    console.log('Clicked login button!'); // Log click action to the console

    navigate('/login'); // Navigate to the login page after button click
  };

  return (
    <div className="center-container">
      <button
        className="get-started-btn"
        onClick={handleClick} // Trigger the handleClick function on button click
      >
        {click ? 'Thanks for clicking' : 'Login'} {/* Change button text based on state */}
      </button>
    </div>
  );
}

export default LoginButton;
