from flask import Flask
from flask_socketio import SocketIO
from routes.websocket_handler_route import register_socket_handlers
from dotenv import load_dotenv

load_dotenv()

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    register_socket_handlers(socketio)
    return app

if __name__ == '__main__':
    app = create_app()
    socketio.init_app(app)
    #print("backend running on port 5000...")
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)