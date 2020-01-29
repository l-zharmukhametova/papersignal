/*
 * https://circuits4you.com
 * 
 * Connecting NodeMCU ESP8266 to WiFi Example
 * 
 */
 
#include <ESP8266WiFi.h>        // Include the Wi-Fi library

const char* ssid     = "14spencer";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "sesameeggroll14spencer";     // The password of the Wi-Fi network

void setup() {
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  delay(10);
  Serial.println('\n');


WiFi.disconnect();
delay(1);  
  WiFi.begin(ssid, NULL);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid);

 // while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
//while (WiFi.waitForConnectResult() != WL_CONNECTED){
 while (WiFi.localIP().toString() == "(IP unset)") {
    Serial.print("\ntest");

    Serial.print('.');
    delay(1500);

  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer
}

void loop() { 
    Serial.println("Connection established!");  

}
