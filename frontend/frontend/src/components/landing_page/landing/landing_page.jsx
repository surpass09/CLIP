import React from "react";
import { motion } from "framer-motion";
import '/Users/suryapasupuleti/Documents/coding/LinkUp/frontend/frontend/src/components/landing_page/landing/landing_page.css'; // Importing the CSS file
import GetStarted from "../get_started/get_started_button";
import LoginButton from "../login_button/login_button";

const LandingPage = () => {
  return (
    <div className="landing-page-container">
      <motion.h1
        className="landing-page-title"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        
      </motion.h1>
      <h1 className="linkup">
        LinkUp
      </h1>

      <p className="landing-page-description">
        Connect with like-minded individuals, expand your network, and find friends with shared interests.
      </p>
      <GetStarted/>
      <LoginButton/>
    </div>
  );
};

export default LandingPage;