from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

rooms = {}

@socketio.on('connect')
def handle_connect():
    pass

@socketio.on('join_room')
def handle_join_room(data):
    room = data.get('room')
    username = data.get('username')
    
    if not room:
        return
    
    join_room(room)
    
    if room not in rooms:
        rooms[room] = {
            'players': [],
            'board': [None] * 9,
            'isXNext': True,
            'winner': None
        }
    
    if len(rooms[room]['players']) < 2:
        rooms[room]['players'].append({'id': request.sid, 'username': username, 'symbol': 'X' if len(rooms[room]['players']) == 0 else 'O'})
    
    emit('room_state', rooms[room], room=room)
    emit('player_info', {'symbol': next((p['symbol'] for p in rooms[room]['players'] if p['id'] == request.sid), None)}, room=request.sid)

@socketio.on('make_move')
def handle_make_move(data):
    room = data.get('room')
    index = data.get('index')
    symbol = data.get('symbol')
    
    if room in rooms:
        room_data = rooms[room]
        if room_data['board'][index] is None and not room_data['winner']:
            current_symbol = 'X' if room_data['isXNext'] else 'O'
            if symbol == current_symbol:
                room_data['board'][index] = symbol
                room_data['isXNext'] = not room_data['isXNext']
                winner = check_winner(room_data['board'])
                if winner:
                    room_data['winner'] = winner
                emit('move_made', room_data, room=room)

@socketio.on('reset_game')
def handle_reset_game(data):
    room = data.get('room')
    if room in rooms:
        rooms[room]['board'] = [None] * 9
        rooms[room]['isXNext'] = True
        rooms[room]['winner'] = None
        emit('game_reset', rooms[room], room=room)

def check_winner(board):
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in lines:
        a, b, c = line
        if board[a] and board[a] == board[b] and board[a] == board[c]:
            return board[a]
    if all(board):
        return 'draw'
    return None

@socketio.on('disconnect')
def handle_disconnect():
    for room, data in list(rooms.items()):
        data['players'] = [p for p in data['players'] if p['id'] != request.sid]
        if not data['players']:
            del rooms[room]
        else:
            emit('player_left', {'id': request.sid}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
