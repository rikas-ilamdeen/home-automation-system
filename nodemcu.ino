#include <ESP8266WiFi.h>

const char* ssid = "Rikas's WiFi";       // WiFi SSID
const char* password = "pass12345";   // WiFi Password

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  server.begin();
  
  pinMode(D1, OUTPUT);  // GPIO5 for light
  pinMode(D2, OUTPUT);  // GPIO4 for fan
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    String request = client.readStringUntil('\r');
    client.flush();

    if (request.indexOf("/light/on") != -1) {
      digitalWrite(D1, HIGH);
    } else if (request.indexOf("/light/off") != -1) {
      digitalWrite(D1, LOW);
    } else if (request.indexOf("/fan/on") != -1) {
      digitalWrite(D2, HIGH);
    } else if (request.indexOf("/fan/off") != -1) {
      digitalWrite(D2, LOW);
    }
    
    client.print("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\nLight: ");
    client.print((digitalRead(D1)) ? "On" : "Off");
    client.print("<br>Fan: ");
    client.print((digitalRead(D2)) ? "On" : "Off");
    client.print("</html>\r\n");
    delay(1);
  }
}
