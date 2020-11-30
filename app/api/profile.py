from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import jsonify
from app.extensions import db
from app.model.profile import Profile, profile_schema


class ProfileApi(Resource):
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        profile = Profile(**body, user_id=user_id)
        db.session.add(profile)
        db.session.commit()
        return {'response': 'Ok'}

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        profile = Profile.query.filter_by(user_id=user_id).first()
        return jsonify(profile_schema.dump(profile))

    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        Profile.query.filter_by(user_id=user_id).update(dict(**body))
        db.session.commit()
        return {"response": "Ok"}
