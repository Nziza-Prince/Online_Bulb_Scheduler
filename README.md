# 💡 Bulb Scheduler (IoT Light Automation)

This project allows users to schedule ON and OFF times for a bulb via a web interface. It combines an Arduino relay controller, Python for serial/MQTT handling, and an HTML/CSS/JS frontend for scheduling.

---

## 📁 Directory Structure

bulb-scheduler/ ├── arduino/ │ └── bulb_controller.ino # Arduino sketch for relay control │ ├── backend/ │ └── controller.py # Python script (MQTT + schedule + serial) │ ├── web/ │ ├── index.html # Main web UI │ └── assets/ │ ├── styles.css # Styling │ └── script.js # MQTT & logic for sending times │ ├── requirements.txt # Python packages └── README.md # This documentation

yaml
Copy
Edit

---

## 🚀 Features

- 🕒 Schedule light ON/OFF times
- 🌐 Web interface for easy time input
- 🔁 MQTT-based message passing
- 📟 Serial control of Arduino relay

---

## 🛠️ Requirements

### Hardware
- Arduino Uno or compatible
- Relay module connected to a bulb
- USB cable

### Software
- Python 3.x
- Mosquitto MQTT broker (cloud or local)
- Arduino IDE
- Modern web browser

---

## 🔧 Setup Instructions

### 1. Flash Arduino
Upload the `bulb_controller.ino` sketch from the `arduino/` folder to your Arduino board using the Arduino IDE.

### 2. Install Python Dependencies
Navigate to `backend/` and install dependencies:

```bash
pip install -r ../requirements.txt
3. Update Serial Port in Python Script
In controller.py, update:

python
Copy
Edit
SERIAL_PORT = 'COM9'  # Change to your actual port (e.g., /dev/ttyUSB0)
4. Run Python Backend
bash
Copy
Edit
cd backend
python controller.py
5. Launch Web UI
Open web/index.html in your browser. The interface lets you set ON and OFF times.

Make sure script.js connects to the MQTT broker over WebSockets (e.g., ws://157.173.101.159:9001).

📡 MQTT Topics

Topic	Description
your/topic	Direct ON/OFF commands
your/topic/on	Scheduled ON time
your/topic/off	Scheduled OFF time
To test manually:

bash
Copy
Edit
mosquitto_pub -h 157.173.101.159 -t your/topic/on -m "11:36"
mosquitto_pub -h 157.173.101.159 -t your/topic/off -m "12:00"
📜 How It Works
Web UI sends time messages over MQTT.

Python backend listens and schedules tasks.

At the right time, it sends ON/OFF to Arduino via serial.

Arduino toggles the relay accordingly.

🔒 Future Improvements
🔐 MQTT authentication

🌍 Flask-based web deployment

📲 Mobile responsiveness

📊 Status feedback from Arduino

👥 Contributors
Irasubiza Saly Nelson

Nkotanyi Nziza Prince

Rukundo Bahati Samuel

Uhirwe Esther Hope

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Let me know if you’d like to add environment variable support, deployment instructions, or CI/CD setup next!