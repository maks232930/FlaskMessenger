from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from sqlalchemy import or_

from app.extensions import db
from app.model.chat import Chat, chats_schema
from app.model.message import Message, messages_schema


class ChatsApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        chats = Chat.query.filter(or_(Chat.first_participant_id == user_id, Chat.second_participant_id == user_id))
        return jsonify(chats_schema.dump(chats))

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        chat = Chat(**body, first_participant_id=user_id)
        db.session.add(chat)
        db.session.commit()
        return {"response": "Ok"}, 200


class ChatApi(Resource):
    @jwt_required
    def get(self, chat_id):
        user_id = get_jwt_identity()
        messages = Message.query.filter(Message.chat_id == chat_id,
                                        or_(Message.chat.first_participant_id == user_id,
                                            Message.chat.second_participant_id == user_id))
        return jsonify(messages_schema.dump(messages))

    @jwt_required
    def post(self, chat_id):
        user_id = get_jwt_identity()
        chat = Chat.query.filter(Chat.id == chat_id,
                                 or_(Chat.first_participant_id == user_id, Chat.second_participant_id == user_id))
        body = request.get_json()
        Message(**body, sender=user_id, chat_id=chat_id)
        return {"response": "Ok"}, 200
