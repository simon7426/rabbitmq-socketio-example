import os
from flask_socketio import SocketIO, emit, join_room
from project import socketio
from flask_restx import Namespace, Resource

winner_namespace = Namespace("Winner")
winner = -1


@winner_namespace.route("/<winner_id>")
class Winner(Resource):
    def get(self, winner_id):
        update_winner(winner_id)
        return {
            "message": f"Updated winner {winner_id}"
        }


SOCKETIO_MESSAGE_QUEUE = os.environ.get(
    "SOCKETIO_MESSAGE_QUEUE", "redis://127.0.0.1:6379/0"
)

socketio_instance = SocketIO(message_queue=SOCKETIO_MESSAGE_QUEUE)


def update_winner(winner_id):
    global winner
    winner  = winner_id
    socketio_instance.emit(
        "status", get_winner(), room="winner", namespace="/winner"
    )


def get_winner():
    global winner
    resp_obj = {
        "winner": winner,
    }
    return resp_obj


def update_celery_task_status():
    socketio_instance.emit(
        "status", get_winner(), room="winner", namespace="/winner"
    )


@socketio.on("join", namespace="/winner")
def on_join():
    join_room("winner")
    # emit("status", get_winner(), room="winner")
