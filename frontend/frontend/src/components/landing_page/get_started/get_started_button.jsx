
import React, { useState } from 'react';
import '../get_started/get_started.css'


function GetStarted() {
    const [clicked, setClicked] = useState(false);
  
    const handleClick = () => {
      setClicked(true);
      console.log('Get Started clicked!');
    };
  
    let buttonText = 'Get Started';
  
    if (clicked) {
      buttonText = 'Thanks for clicking!';
    }
  
    return (
      <div className="center-container">
        <button 
          className="get-started-btn" 
          onClick={handleClick}
        >
          {buttonText}
        </button>
      </div>
    );
  }
  
  export default GetStarted;
  