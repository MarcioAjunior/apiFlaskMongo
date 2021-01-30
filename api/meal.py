from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


from models.meals import Meals
from api.errors import forbidden
from models.users import Users

class MealsApi(Resource):
  
    @jwt_required
    def get(self):
       
        output = Meals.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self):
        
        authorized : bool = Users.objects.get(id=get_jwt_identity()).access.admin
        
        if authorized:
            data = request.get_json()
            post_user = Meals(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()


class MealApi(Resource):
   
    @jwt_required
    def get(self, meal_id: str):
        
        output = Meals.objects.get(id=meal_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, meal_id: str) :
        
        data = request.get_json()
        put_user = Meals.objects(id=meal_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id: str) :

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Meals.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()