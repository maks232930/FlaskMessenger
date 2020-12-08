from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import jsonify
from app.extensions import db
from app.model.profile import Profile, profile_schema


class ProfileApi(Resource):
    @jwt_required
    def post(self, user_id):
        authorized_user_id = int(get_jwt_identity())
        if user_id != authorized_user_id:
            return {"Response": "user_id invalid"}, 404
        body = request.get_json()
        profile = Profile(**body, user_id=user_id)
        db.session.add(profile)
        db.session.commit()
        return {"Response": "Created"}, 201

    @jwt_required
    def get(self, user_id):
        profile = Profile.query.filter_by(user_id=user_id).first()
        if profile is None:
            return {"Response": "No profile"}, 401
        return jsonify(profile_schema.dump(profile), 200)

    @jwt_required
    def put(self, user_id):
        authorized_user_id = get_jwt_identity()
        if user_id != authorized_user_id:
            return {"Response": "user_id invalid"}, 401
        body = request.get_json()
        print(len(body['last_name']))
        Profile.query.filter_by(user_id=user_id).update(dict(**body))
        db.session.commit()
        return {"response": "Ok"}, 200
