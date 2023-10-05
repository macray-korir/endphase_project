from app import app
from models import db, User, Meal, Ingredient
from faker import Faker
import random

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Users
    users = []
    for _ in range(20):
        user = User(
            username=fake.user_name(),
            password_hash=fake.password(),
            email=fake.email(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    meals = []
    ingredients = []

    for _ in range(30):
        meal = Meal(
            title=fake.catch_phrase(),
            description=fake.text(),
            category=fake.word(),
            user_id=random.randint(1, 20), 
        )
        db.session.add(meal)
        db.session.flush()  

        for _ in range(random.randint(2, 5)):
            ingredient = Ingredient(
                name=fake.word(),
                quantity=random.uniform(0.1, 5.0),
                unit=fake.word(),
                meal_id=meal.id,  
            )
            ingredients.append(ingredient)

    db.session.add_all(ingredients)
    db.session.commit()


print("Seed completed!")
