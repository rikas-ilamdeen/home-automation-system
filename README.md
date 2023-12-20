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

#### Installation

1. Connect an LED to GPIO pin 17 on your Raspberry Pi.
2. Clone this repository to your Raspberry Pi.
    ```bash
    git clone https://github.com/your-username/rpi-led-control.git
    ```
3. Install dependencies.
    ```bash
    pip install Flask RPi.GPIO
    ```

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

#### Project Structure

- `app.py`: Flask application for controlling the LED.
- `templates/index.html`: HTML template for the web interface.

#### Configuration

- The LED is connected to GPIO pin 17. You can modify this in the `app.py` file if needed.
