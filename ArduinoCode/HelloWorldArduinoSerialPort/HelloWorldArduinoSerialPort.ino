void setup() {
  // Initialize the serial communication at 9600 baud rate
  Serial.begin(9600);
}

void loop() {
  // Send the message "Hello, World!" to the serial port
  Serial.println("Hello, World!");
  // Delay for 1 second before sending the message again
  delay(1000);
}
