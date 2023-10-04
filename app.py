from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreta!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('new_message')
def handle_new_message(data):
    message = data['message']
    recipient = data['recipient']
    send({'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)