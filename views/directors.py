from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        red_json = request.json
        director_service.create(red_json)
        return "Director created", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid: int):
        try:
            director = director_service.get_one(uid)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def put(self, uid: int):
        red_json = request.json
        red_json["id"] = uid
        director_service.update(red_json)
        return "Director updated", 204

    @admin_required
    def delete(self, uid: int):
        director_service.delete(uid)
        return "Director deleted", 204
