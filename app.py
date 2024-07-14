import RPi.GPIO as GPIO     # library for working with GPIO pins on the Raspberry Pi
from flask import Flask, render_template, request, redirect, url_for  # classes and functions from the Flask library

app = Flask(__name__)       # Flask application setup

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO mode and channel
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

@app.route("/")     
def home():                     # Defines a route for the home page
    return render_template("index.html")

@app.route("/on")
def turn_on():
    GPIO.output(17, GPIO.HIGH)  # Turn the LED on
    return "LED turned on!"

@app.route("/off")
def turn_off():
    GPIO.output(17, GPIO.LOW)  # Turn the LED off
    return "LED turned off!"

if __name__ == "__main__":          # Checks if the script is being run directly (not imported as a module)
    app.run(host="0.0.0.0", port=5000, debug=True)      # starts the Flask application on host 
