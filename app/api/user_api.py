from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.extensions import db
from app.model.user import User, user_schema


class UserApi(Resource):
    @jwt_required
    def get(self, user_id):
        authorized_id = get_jwt_identity()
        if user_id != authorized_id:
            return {"Response": "user_id invalid"}, 401
        user = User.query.filter_by(id=user_id).first()
        return jsonify(user_schema.dump(user))

    @jwt_required
    def put(self, user_id):
        authorized_id = get_jwt_identity()
        if user_id != authorized_id:
            return {"Response": "user_id invalid"}, 401
        body = request.get_json()
        User.query.filter_by(id=user_id).update(dict(**body))
        db.session.commit()
        return {'response': 'Ok'}, 200

    @jwt_required
    def delete(self, user_id):
        authorized_id = get_jwt_identity()
        if user_id != authorized_id:
            return {"Response": "user_id invalid"}, 401
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        return {'Response': 'Ok'}, 204
