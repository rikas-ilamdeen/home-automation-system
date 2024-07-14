# Smart Home Automation System

Control home devices remotely with a web interface using Raspberry Pi and NodeMCU ESP8266. This project allows to control multiple devices such as lights and fans through a user-friendly web interface.

## Features

- **Web Interface:** Control connected devices through a user-friendly web page.
- **Raspberry Pi Integration:** The Flask-based web server runs on a Raspberry Pi for local control.
- **NodeMCU Integration:** Use NodeMCU ESP8266 to control devices over Wi-Fi.
- **Multiple Device Control:** Manage multiple devices such as lights, fans, etc.

## Requirements

- Raspberry Pi with GPIO support
- NodeMCU ESP8266
- Relay modules (for controlling high-power devices)
- Python installed on Raspberry Pi
- Flask Python library
- Arduino IDE (for programming NodeMCU)
- Wi-Fi network

#### Installation

1. **Set up the hardware:**
   - Connect devices (e.g., lights, fans) to relay modules.
   - Connect relay modules to the GPIO pins of Raspberry Pi and NodeMCU ESP8266.

2. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/rpi-led-control.git
    ```

3. **Install dependencies on Raspberry Pi:**
    ```bash
    pip install Flask RPi.GPIO requests
    ```

4. **Program the NodeMCU ESP8266:**
   - Use the Arduino IDE to upload the provided NodeMCU code.

5. **Update Wi-Fi credentials:**
   - Update the `ssid` and `password` in the NodeMCU code with Wi-Fi network credentials.

#### Running the Project

1. **Open a terminal on Raspberry Pi.**

2. **Navigate to the project directory.**
    ```bash
    cd path/to/rpi-led-control
    ```

3. **Run the Flask application.**
    ```bash
    python app.py
    ```

4. **Access the web interface:**
   - Open a web browser and go to `http://<your_pi_ip>:5000` to access the LED control interface.

5. **Use the provided buttons to turn the devices On and Off.**

6. **To stop the Flask application, return to the terminal and press `Ctrl+C` to interrupt the process.**

#### Project Structure

- **app.py**                  # Main Flask application
- **nodemcu.ino**             # NodeMCU ESP8266 code
- **requirements.txt**        # List of dependencies
- **templates/index.html**    # HTML template for the web interface
- **static/styles.css**       # CSS for the web interface
- **README.md**               # Project documentation

#### Configuration

- Update the GPIO pin numbers and device types in `app.py` and `nodemcu.ino`
