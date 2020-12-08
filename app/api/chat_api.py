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
        print(len(body['name']))
        chat = Chat(**body, first_participant_id=user_id)
        print(len(chat.name))
        db.session.add(chat)
        db.session.commit()
        return {"Response": "Created"}, 201


class ChatApi(Resource):
    @jwt_required
    def get(self, chat_id):
        user_id = get_jwt_identity()
        chat = Chat.query.filter(Chat.id == chat_id,
                                 or_(Chat.first_participant_id == user_id,
                                     Chat.second_participant_id == chat_id)).filter(Message.is_delete != False)
        if chat is None:
            return {"Response": "chat_id invalid"}, 404
        messages = Message.query.join(Chat).filter(Message.chat_id == Chat.id).filter(Message.chat_id == chat_id)
        return jsonify(messages_schema.dump(messages))

    @jwt_required
    def post(self, chat_id):
        user_id = get_jwt_identity()
        chat = Chat.query.filter(Chat.id == chat_id,
                                 or_(Chat.first_participant_id == user_id,
                                     Chat.second_participant_id == user_id)).first()
        if chat is None:
            return {"response": "chat_id invalid"}, 404
        body = request.get_json()
        message = Message(**body, sender_id=user_id, chat=chat)
        db.session.add(message)
        db.session.commit()
        return {"response": "Ok"}, 201
