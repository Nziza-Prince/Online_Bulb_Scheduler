import serial
import subprocess

SERIAL_PORT = '/dev/ttyACM0'  # Replace with your port
BAUD_RATE = 9600

try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Connected to Arduino.")
except Exception as e:
    print(f"Serial error: {e}")
    exit()

print("Listening for MQTT messages...")

# Run mosquitto_sub and read line-by-line
proc = subprocess.Popen(
    ["mosquitto_sub", "-h", "localhost", "-t", "iot/light"],
    stdout=subprocess.PIPE,
    text=True
)

try:
    for line in proc.stdout:
        msg = line.strip()
        print(f"Received MQTT message: {msg}")
        if msg == "ON":
            arduino.write(b'1')
        elif msg == "OFF":
            arduino.write(b'0')
except KeyboardInterrupt:
    print("Stopping...")
    proc.kill()
    arduino.close()
