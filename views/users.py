from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from decorators import admin_required
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)
        return response, 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route("/<int:uid>")
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

