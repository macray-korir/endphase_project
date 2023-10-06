import React from 'react';
import { Link } from 'react-router-dom';


function Contact() {
  return (
    <div
      className="hero"
      style={{
        width: '100%',
        height: '100vh',
        backgroundImage: 'url("/image2.jpg")',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        objectFit: 'cover',
        position: 'relative',
      }}
    >
      <div className="overlay">
        <div className='hero-header'>
          <h1>Need Help?</h1>
        </div>
        <h3> If you have inquiries or need assistance, do not hesitate to chat with us.</h3>
        <h3>We're available from Monday to Sunday, between 8am and 8pm.</h3>
        <h3>You can also reach us on 0711011011 from Monday to Friday</h3>


        {/* <Link to="/feedback">
          <button className="btn-custom">Give Feedback</button>
        </Link> */}
      </div>
    </div>
  );
}

export default Contact;
