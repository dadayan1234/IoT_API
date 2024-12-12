from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

data_store = {}  # Menyimpan data payload secara dinamis

# Swagger setup
SWAGGER_URL = '/api/docs'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # Path to the API documentation JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask IoT API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    """
    Receive IoT data
    ---
    tags:
      - IoT Data
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              charts:
                type: array
                items:
                  type: object
                  properties:
                    chart_name:
                      type: string
                      example: Temperature
                    value:
                      type: number
                      example: 25
    responses:
      200:
        description: Data received successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                data:
                  type: object
      400:
        description: Error processing data
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                error:
                  type: string
    """
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