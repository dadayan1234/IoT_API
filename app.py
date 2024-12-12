from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

data_store = {}  # Menyimpan data payload secara dinamis

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        payload = request.json
        charts = payload.get('charts', [])

        for chart in charts:
            chart_name = chart.get('chart_name', 'default')
            value = chart.get('value', 0)
            
            # Simpan data pada data_store
            data_store[chart_name] = value

            # Broadcast data ke client
            socketio.emit('update_data', {'chart_name': chart_name, 'value': value})
        
        return jsonify({'message': 'Data received successfully', 'data': payload}), 200
    except Exception as e:
        return jsonify({'message': 'Error processing data', 'error': str(e)}), 400

if __name__ == '__main__':
    socketio.run(app)
