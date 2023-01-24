from flask import Flask
from flask_restful import Resource, Api

from main import chat

app = Flask(__name__)
api = Api(app)

class ChatXGPT(Resource):
    def get(self, user_input):
        response = chat(user_input)
        return response
    
api.add_resource(ChatXGPT, "/chat/<user_input>")

if __name__ == "__main__":
    app.run(port=6969)

