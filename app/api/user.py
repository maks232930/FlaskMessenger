from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.extensions import db
from app.model.user import User, user_schema


class UserApi(Resource):
    @jwt_required
    def get(self, user_id):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        return jsonify(user_schema.dump(user))

    @jwt_required
    def put(self, user_id):
        user_id = get_jwt_identity()
        body = request.get_json()
        User.query.filter_by(id=user_id).update(dict(**body))
        db.session.commit()
        return {'response': 'Ok'}, 200