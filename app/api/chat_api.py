from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from sqlalchemy import or_

from app.extensions import db
from app.model.chat import Chat, chats_schema
from app.model.message import Message


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
        messages = Message.query(Message.chat_id == chat_id)
        messages.filter(Message.chat.second_participant_id == user_id)
        # ses.query(FooBar).join(Foobar.bar).join(Bar.foo).filter(Foo.name == "blah")

        # if messages is None:
        #     return {'response': "Not Found"}, 404
        # return jsonify(messages_schema.dump(messages))
        return "None"

    # @jwt_required
    # def post(self, chat_id):
    #     user_id = get_jwt_identity()
    #     chat = Chat.query.filter(Chat.id == chat_id,
    #                              or_(Chat.first_participant_id == user_id, Chat.second_participant_id == user_id))
    #     body = request.get_json()
    #     Message(**body, sender=user_id, chat_id=chat_id)
    #     return {"response": "Ok"}, 200
