from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from flask_swagger_ui import get_swaggerui_blueprint
from db_helper import DBHelper
import config

# Flask app and SocketIO setup
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['DEBUG'] = config.DEBUG

socketio = SocketIO(app)

data_store = {}  # Menyimpan data payload secara dinamis
db_helper = DBHelper(config.DB_NAME)  # Initialize SQLite database

# Swagger setup
SWAGGER_URL = '/docs'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # Path to the API documentation JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask IoT API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        payload = request.json
        charts = payload.get('charts', [])

        for chart in charts:
            chart_name = chart.get('chart_name', 'default')
            value = chart.get('value', 0)

            # Simpan data ke data_store dan SQLite
            data_store[chart_name] = value
            db_helper.insert_data(chart_name, value)

            # Broadcast data ke client
            socketio.emit('update_data', {'chart_name': chart_name, 'value': value})

        return jsonify({'message': 'Data received successfully', 'data': payload}), 200
    except Exception as e:
        return jsonify({'message': 'Error processing data', 'error': str(e)}), 400

@app.route('/data', methods=['GET'])
def get_data():
    try:
        chart_name = request.args.get('chart_name')
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')

        # Ambil data berdasarkan query
        data = db_helper.get_filtered_data(chart_name, start_time, end_time)
        return jsonify({'message': 'Data retrieved successfully', 'data': data}), 200
    except Exception as e:
        return jsonify({'message': 'Error retrieving data', 'error': str(e)}), 400

if __name__ == '__main__':
    socketio.run(app)