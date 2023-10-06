import React, { useEffect, useState } from 'react';

function Meals() {
  const [meals, setMeals] = useState([]);

  useEffect(() => {
    // Make a GET request to your Flask API
    fetch('/meal')
      .then((response) => response.json())
      .then((data) => {
        setMeals(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Meals</h1>
      <ul>
        {meals.map((meal) => (
          <li key={meal.id}>
            <h2>{meal.title}</h2>
            <p>{meal.description}</p>
            <p>Category: {meal.category}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Meals;
