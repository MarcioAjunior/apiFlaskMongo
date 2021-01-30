from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


from models.users import Users
from api.errors import forbidden


class UsersApi(Resource):
    
    @jwt_required
    def get(self):
        
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects()
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def delete(self) :
        
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects.delete()
            return jsonify({'result': output})
        else:
            return forbidden()


class UserApi(Resource):
   
    @jwt_required
    def get(self, user_id: str):
       
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects.get(id=user_id)
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def put(self, user_id: str):

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Users.objects(id=user_id).update(**data)
            output = {'id': str(put_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def post(self):
      
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Users(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required
    def delete(self, user_id: str):
     
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()