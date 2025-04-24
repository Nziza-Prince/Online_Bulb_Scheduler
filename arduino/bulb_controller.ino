int relayPin = 2;
void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH); // OFF initially
}
void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(relayPin, LOW);  // Turn ON
    } else if (command == '0') {
      digitalWrite(relayPin, HIGH); // Turn OFF
    }
  }
}
