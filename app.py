import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO mode and channel
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Assuming you are using GPIO 17

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/on")
def turn_on():
    GPIO.output(17, GPIO.HIGH)  # Turn the LED on
    return "LED turned on!"

@app.route("/off")
def turn_off():
    GPIO.output(17, GPIO.LOW)  # Turn the LED off
    return "LED turned off!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
