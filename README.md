This project implements an Anti-Theft Intrusion Detection System using a Raspberry Pi, a PIR motion sensor, and a camera module. The system detects motion in a monitored area, captures an image of the intruder, and sends an email alert with the captured image to the user/owner. It also integrates a door sensor to monitor the state of a door (open/closed) and triggers motion detection when the door is open.

**Table of Contents****
Features
Hardware Requirements
Software Requirements
Setup Instructions
How It Works
Code Overview
Customization
Troubleshooting
License
Author

**Features**
Motion Detection: Utilizes a PIR motion sensor to detect intruders.
Image Capture: Captures high-quality images using the Raspberry Pi camera module.
Email Alerts: Sends real-time email notifications with the captured image to the user/owner.
Door Sensor Integration: Monitors the state of a door (open/closed) to trigger motion detection.
Scalable Design: Easily customizable for different use cases, such as home security or office monitoring.

**Hardware Requirements**
To build this project, you will need the following components:

**Raspberry Pi (any model with GPIO pins and camera support).
PIR Motion Sensor (for detecting motion).
Raspberry Pi Camera Module (compatible with the Raspberry Pi).
Door Sensor (optional, for monitoring door state).
Jumper Wires (for connecting components).
Power Supply (for the Raspberry Pi and sensors).**

**Software Requirements**
Python 3.x (installed on the Raspberry Pi).

**Required Python Libraries:**

**smtplib (for sending emails).
picamera2 (for controlling the Raspberry Pi camera).
RPi.GPIO (for GPIO pin control).
gpiozero (for interfacing with the PIR sensor).
email.mime (for creating email attachments).**

Install the required libraries using the following command:

**bash
Copy
pip install picamera2 RPi.GPIO gpiozero**
Setup Instructions
**1. Hardware Setup**
Connect the PIR Motion Sensor to GPIO pin 4.
Connect the Door Sensor to GPIO pin 16.
Attach the Raspberry Pi Camera Module to the Raspberry Pi.
Ensure all connections are secure and the Raspberry Pi is powered on.

**2. Configure Gmail SMTP**
To send emails, you need to:
Enable Less Secure Apps or generate an App Password in your Gmail account settings.
Update the following variables in the script with your Gmail credentials:


**3. Run the Script**
Save the provided Python script as anti_theft.py and run it on your Raspberry Pi:
The system continuously monitors the state of the door sensor.
If the door is open, it checks for motion using the PIR sensor.
**When motion is detected:**
**The Raspberry Pi camera captures an image of the intruder.
The image is saved locally and attached to an email.
An email alert is sent to the user/owner with the captured image.
The system repeats the process until manually stopped.**
Code Overview
The Python script is structured as follows:

**Emailer Class: Handles sending emails with captured images using Gmail's SMTP server.
Camera Setup: Configures and controls the Raspberry Pi camera module.
Motion Detection: Uses the PIR sensor to detect intruders.
Door Sensor Integration: Monitors the door state to trigger motion detection.
Main Loop: Continuously checks for door state and motion, triggering alerts as needed.**


Customization

**Email Recipient: Update the sendTo variable in the script to change the recipient's email address.
Image Path: Modify the image variable to save the captured image to a different location.
Sensor Pins: Change the GPIO pin numbers in the script if using different pins.
Email Content: Customize the email subject and body in the sendmail function.**

Troubleshooting

**Email Not Sent:
Ensure the Gmail credentials are correct.
Check if "Less Secure Apps" or "App Password" is enabled in your Gmail account.**

Camera Not Working:

Verify the camera module is properly connected and enabled in Raspberry Pi settings.

Sensor Issues:

Double-check the wiring and GPIO pin connections.

License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.
