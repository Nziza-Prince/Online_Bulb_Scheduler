import serial
import schedule
import time
from datetime import datetime
import paho.mqtt.client as mqtt
SERIAL_PORT = 'COM9'
BAUD_RATE = 9600
MQTT_BROKER = "157.173.101.159"
MQTT_PORT = 1883
TOPIC_COMMAND = "your/topic"
TOPIC_SCHEDULE_ON = "your/topic/on"
TOPIC_SCHEDULE_OFF = "yout/topic/off"
# Serial connection
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print("Connected to Arduino")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()
# Light control functions
def turn_on_light():
    arduino.write(b'ON\n')
    print(f"[{datetime.now()}] Sent: ON")
def turn_off_light():
    arduino.write(b'OFF\n')
    print(f"[{datetime.now()}] Sent: OFF")
# Scheduler clear and reschedule
def set_schedule(on_time, off_time):
    schedule.clear()
    schedule.every().day.at(on_time).do(turn_on_light)
    schedule.every().day.at(off_time).do(turn_off_light)
    print(f":date: Schedule set: ON at {on_time}, OFF at {off_time}")
# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print(f":electric_plug: Connected to MQTT broker with result code {rc}")
    client.subscribe(TOPIC_COMMAND)
    client.subscribe(TOPIC_SCHEDULE_ON)
    client.subscribe(TOPIC_SCHEDULE_OFF)
def on_message(client, userdata, msg):
    global on_time, off_time
    topic = msg.topic
    message = msg.payload.decode().strip()
    print(f"[MQTT] {topic}: {message}")
    if topic == TOPIC_COMMAND:
        if message == "ON":
            turn_on_light()
        elif message == "OFF":
            turn_off_light()
    elif topic == TOPIC_SCHEDULE_ON:
        try:
            time.strptime(message, "%H:%M")
            on_time = message
            if off_time:
                set_schedule(on_time, off_time)
        except ValueError:
            print(":exclamation: Invalid ON time format")
    elif topic == TOPIC_SCHEDULE_OFF:
        try:
            time.strptime(message, "%H:%M")
            off_time = message
            if on_time:
                set_schedule(on_time, off_time)
        except ValueError:
            print("Invalid OFF time format")
# Global schedule times
on_time = ""
off_time = ""
# Main
if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    print(":satellite_antenna: Listening for MQTT commands and schedules...")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        client.loop_stop()
        arduino.close()