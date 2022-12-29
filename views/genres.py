from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        red_json = request.json
        genre_service.create(red_json)
        return "Genre created", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, uid: int):
        try:
            genre = genre_service.get_one(uid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def put(self, uid: int):
        red_json = request.json
        red_json["id"] = uid
        genre_service.update(red_json)
        return "Genre updated", 204

    @admin_required
    def delete(self, uid: int):
        genre_service.delete(uid)
        return "Genre deleted", 204
