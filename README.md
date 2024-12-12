# 🏙️ **IoT Sensor Simulator for Smart City** 🌱

Welcome to the **IoT Sensor Simulator**! 🚀  
This project was developed by **Dian Prasetya** as a reference for **IoT for Smart Cities** course. 🧑‍🏫📚  
The goal of this project is to simulate IoT sensors for monitoring environmental factors like **Temperature**, **Humidity**, and **LDR (Light Dependent Resistor)**. The data is dynamically generated and sent to a server to be visualized in real-time.

## 🎯 **Project Overview**
This project showcases a simulation where IoT devices (sensors) generate data and send it to a Flask-based backend. The data is visualized using a modern real-time dashboard, making it an excellent reference for **Smart City IoT** applications. The backend uses **Flask**, **SocketIO**, and **Swagger UI** for API documentation, while the frontend utilizes **HTML5**, **Bootstrap**, and **ToastUI** for chart visualizations.

---

## 🛠️ **Technologies Used**

### Backend:
- **Flask**: A lightweight web framework for Python, used to handle HTTP requests and WebSocket communication.
- **SocketIO**: Real-time bidirectional communication between the server and clients.
- **Swagger UI**: For documenting the IoT API for easy integration and testing.

### Frontend:
- **HTML5**: Markup language to structure the data visualization dashboard.
- **Bootstrap 5**: Responsive and modern UI framework for building sleek and clean user interfaces.
- **ToastUI**: For rendering real-time gauge charts to visualize IoT data.

### Simulator:
- **Python**: Used for the sensor simulator to generate random sensor data and send it to the backend using **HTTP POST** requests.

---

## 📦 **Getting Started**

### 1️⃣ **Clone the Repository**

```bash

git clone https://github.com/your-repo/IoT-Sensor-Simulator.git
cd IoT-Sensor-Simulator

```

---

### 2️⃣ **Install Dependencies**
Create a virtual environment and install the necessary dependencies.

```bash
Salin kode
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Windows, use venv\Scripts\activate
# Install the dependencies
pip install -r requirements.txt
```

---

### 3️⃣ **Start the Server**
Run the Flask server to start the application.

```bash
# Run the server
python app.py
```
The server will be running at http://localhost:5000.

---

### 4️⃣ **Run the Sensor Simulator**
Run the simulator script that will send data to the server every 2 seconds.

```bash
Salin kode
python client.py

```

---

### 5️⃣ **Access the Dashboard**
Visit http://localhost:5000 in your browser to access the real-time dashboard.

