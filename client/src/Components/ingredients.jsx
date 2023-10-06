import React, { useEffect, useState } from 'react';

function Ingredients() {
  const [ingredients, setIngredients] = useState([]);

  useEffect(() => {
    fetch('/ingredient')
      .then((response) => response.json())
      .then((data) => {
        setIngredients(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Ingredients</h1>
      <ul>
        {ingredients.map((ingredient) => (
          <li key={ingredient.id}>
             <p>{ingredient.name}</p>
             <p>{ingredient.quantity}</p>
             <p> {ingredient.unit}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Ingredients;
