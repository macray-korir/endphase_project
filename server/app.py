from flask import Flask, make_response, jsonify,request
from models import db, User,Meal,Ingredient
from flask_restful import Resource, Api
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///endphase.db'
db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return {"hello": "Welcome to my API"}

class UsersResource(Resource):
    def get(self):
        user_list = []
        for user in User.query.all():
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
            user_list.append(user_dict)

        response = make_response(
            jsonify(user_list),
            200
        )
        return response
    def post(self):
        user_data = request.get_json()
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')  # You may need to hash the password

        # Validate and handle the data as needed
        if not username or not email or not password:
            return {"error": "Missing required fields"}, 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        response_data = {
            "message": "New User created successfully",
            "user_id": new_user.id
        }

        return response_data, 201

api.add_resource(UsersResource, '/users')

class UserResource(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                # "created_at": user.created_at,
            }
            return user_data, 200
        else:
            return {"error": "User not found"}, 404

api.add_resource(UserResource, '/users/<int:id>')

class MealResource(Resource):
    def get(self, id=None):
     if id is None:
        meal_list = []
        for meal in Meal.query.all():
            meal_dict = {
                "id": meal.id,
                "title": meal.title,
                "description": meal.description,
                "category": meal.category
            }
            meal_list.append(meal_dict)

        response = make_response(
            jsonify(meal_list),
            200
        )
        return response
     else:
        meal = Meal.query.filter_by(id=id).first()
        if meal:
            meal_data = {
                "id": meal.id,
                "title": meal.title,
                "description": meal.description,
                "category": meal.category
            }
            return meal_data, 200
        else:
            return {"error": "Meal not found"}, 404

    def post(self):
        meal_data = request.get_json()
        title = meal_data.get('title')
        description = meal_data.get('description')
        category = meal_data.get('category')

        if not title or not description or not category:
            return {"error": "Missing required fields"}, 400

        new_meal = Meal(title=title, description=description, category=category)
        db.session.add(new_meal)
        db.session.commit()

        response_data = {
            "message": "New Meal created successfully",
            "meal_id": new_meal.id
        }

        return response_data, 201
    
    def patch(self, id):
        meal = Meal.query.filter_by(id=id).first()
        if not meal:
            return {"error": "Meal not found"}, 404

        meal_data = request.get_json()

        if 'title' in meal_data:
            meal.title = meal_data['title']
        if 'description' in meal_data:
            meal.description = meal_data['description']
        if 'category' in meal_data:
            meal.category = meal_data['category']

        db.session.commit()
        return {"message": "Recipe updated successfully"}, 200

    def delete(self, id):
        meal= Meal.query.filter_by(id=id).first()
        if not meal:
            return {"error": "meal not found"}, 404

        db.session.delete(meal)
        db.session.commit()
        return {"message": "Meal deleted successfully"}, 200

api.add_resource(MealResource, '/meal', '/meal/<int:id>')

class IngredientResource(Resource):
    def get(self, id=None):
        if id is None:
            ingredient_list = []
            for ingredient in Ingredient.query.all():
                ingredient_dict = {
                    "id": ingredient.id,
                    "name": ingredient.name,
                    "quantity": ingredient.quantity,
                    "unit": ingredient.unit
                }
                ingredient_list.append(ingredient_dict)

            response = make_response(
                jsonify(ingredient_list),
                200
            )
            return response
        else:
            ingredient = Ingredient.query.filter_by(id=id).first()
            if ingredient:
                ingredient_data = {
                    "id": ingredient.id,
                    "name": ingredient.name,
                    "quantity": ingredient.quantity,
                    "unit": ingredient.unit
                }
                return ingredient_data, 200
            else:
                return {"error": "Ingredient not found"}, 404
    def post(self):
        ingredient_data = request.get_json()
        name = ingredient_data.get('name')
        quantity = ingredient_data.get('quantity')
        unit = ingredient_data.get('unit')

        if not name or not quantity or not unit:
            return {"error": "Missing required fields"}, 400

        new_ingredient = Ingredient(name=name, quantity=quantity, unit=unit)
        db.session.add(new_ingredient)
        db.session.commit()

        response_data = {
            "message": "New Ingredient created successfully",
            "ingredient_id": new_ingredient.id
        }

        return response_data, 201
    def patch(self, id):
        ingredient = Ingredient.query.filter_by(id=id).first()
        if not ingredient:
            return {"error": "Ingredient not found"}, 404

        ingredient_data = request.get_json()
        if 'name' in ingredient_data:
            ingredient.name = ingredient_data['name']
        if 'quantity' in ingredient_data:
            ingredient.quantity = ingredient_data['quantity']
        if 'unit' in ingredient_data:
            ingredient.unit = ingredient_data['unit']

        db.session.commit()
        return {"message": "Ingredient updated successfully"}, 200

    def delete(self, id):
        ingredient = Ingredient.query.filter_by(id=id).first()
        if not ingredient:
            return {"error": "Ingredient not found"}, 404

        db.session.delete(ingredient)
        db.session.commit()
        return {"message": "Ingredient deleted successfully"}, 200

api.add_resource(IngredientResource, '/ingredient', '/ingredient/<int:id>')



if __name__ == '__main__':
    app.run(debug=True)
