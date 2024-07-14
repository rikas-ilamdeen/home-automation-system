import RPi.GPIO as GPIO     # library for working with GPIO pins on the Raspberry Pi
from flask import Flask, render_template, request, redirect, url_for  # classes and functions from the Flask library
import requests

app = Flask(__name__)       # Flask application setup

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO mode and channels
GPIO.setmode(GPIO.BCM)
devices = {
    'light': 17,
    'fan': 27,
    'ac': 22
}

for device, pin in devices.items():
    GPIO.setup(pin, GPIO.OUT)

nodemcu_ip = "192.168.1.10"  # NodeMCU IP address

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<device>/<action>")
def control_device(device, action):
    if device in devices:
        if action == "on":
            GPIO.output(devices[device], GPIO.HIGH)
        elif action == "off":
            GPIO.output(devices[device], GPIO.LOW)
    else:
        # For devices controlled by NodeMCU
        requests.get(f"http://{nodemcu_ip}/{device}/{action}")
    return redirect("/")

if __name__ == "__main__":          # Checks if the script is being run directly (not imported as a module)
    app.run(host="0.0.0.0", port=5000, debug=True)      # starts the Flask application on host 
