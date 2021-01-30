from flask_restful import Api


from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.meal import MealsApi, MealApi


def create_routes(api: Api):
    
    api.add_resource(SignUpApi, '/authentication/signup')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(MealsApi, '/meal')
    api.add_resource(MealApi, '/meal/<meal_id>')