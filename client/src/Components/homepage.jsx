import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <>
      <div
        className="hero"
        style={{
          width: '100%',
          height: '100vh',
          backgroundImage: 'url("./public/image3.jpg")',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          objectFit: 'cover',
          position: 'relative',
        }}
      >
        <div className="overlay">
          <h1>Welcome to MealBox</h1>
          <h3>
            Where the taste is so delicious,it'll linger in your memory forOever!
          </h3>
          <div className="buttons-container">
            <Link to="/meal" className="btn-custom">
              Meals
            </Link>
            <Link to="/contact" className="btn-custom">
              Ingredients
            </Link>
            <Link to="/contact" className="btn-custom">
              Contact Us
            </Link>
          </div>
        </div>
      </div>
    </>
  );
}

export default HomePage;
