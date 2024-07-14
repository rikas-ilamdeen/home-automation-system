# Raspberry Pi based Home Automation System
Control your home devices remotely with a web interface. This project includes a Flask-based web server on Raspberry Pi.

### Features
- **Web Interface:** Control connected devices through a user-friendly web page.
- **Raspberry Pi Integration:** The Flask-based web server runs on a Raspberry Pi for local control.

#### Requirements
- Raspberry Pi with GPIO support
- Relay module (if controlling high-power devices)
- Python installed on Raspberry Pi
- Flask Python library

#### Running the Project
1. Open a terminal on your Raspberry Pi.
2. Navigate to the project directory.
    ```bash
    cd path/to/rpi-led-control
    ```
3. Run the Flask application.
    ```bash
    python app.py
    ```
4. Open a web browser and go to `http://<your_pi_ip>:5000` to access the LED control interface.
5. Use the provided buttons to turn the LED on and off.
6. To stop the Flask application, return to the terminal and press `Ctrl+C` to interrupt the process.

#### Improve
- Mobile app (android and ios)
- connect many devices (high voltage)
- NodeMCU ESP32 (low cost)