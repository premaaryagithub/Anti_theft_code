import smtplib
import time
from picamera2 import Picamera2, Preview
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
from gpiozero import MotionSensor

# Initialize the camera
cam = Picamera2()

# Set up PIR sensor
PIR_PIN = MotionSensor(4)  # Set GPIO pin for PIR sensor

# Email Variables
SMTP_SERVER = 'smtp.gmail.com'  # Email Server (don't change!)
SMTP_PORT = 587  # Server Port (don't change!)
GMAIL_USERNAME = 'premsaidulla@gmail.com'  # Change this to match your Gmail account
GMAIL_PASSWORD = 'iyhb fwtk uypx slsy'  # Change this to match your Gmail App Password

# Emailer Class
class Emailer:
    def sendmail(self, recipient, subject, content, image):
        # Create Email Headers
        emailData = MIMEMultipart()
        emailData['subject'] = subject
        emailData['to'] = recipient
        emailData['from'] = GMAIL_USERNAME
        
        # Attach text content
        emailData.attach(MIMEText(content))
        
        # Attach the image
        with open(image, 'rb') as img_file:
            imageData = MIMEImage(img_file.read(), 'jpg')
            imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
            emailData.attach(imageData)

        # Connect to Gmail Server and send the email
        try:
            session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            session.ehlo()
            session.starttls()
            session.ehlo()

            # Login to Gmail
            session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

            # Send the email
            session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            session.quit()  # Close the session

# Create an instance of the Emailer class
sender = Emailer()

# Define the image file path
image = '/home/anti/image.jpg'  # Ensure the path is correct

# Set the GPIO mode to BCM for the door sensor
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number to which the door sensor is connected
DOOR_SENSOR_PIN = 16

# Setup the GPIO pin as an input
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the door sensor (HIGH when open, LOW when closed)
        door_state = GPIO.input(DOOR_SENSOR_PIN)
        
        if door_state == GPIO.HIGH:  # Door is OPEN
            print("Door is OPEN")
            print("Checking for motion...")

            # Check for motion detection
            if PIR_PIN.wait_for_active(timeout=5):  # Wait for motion detection with a timeout
                print("Motion detected, sending image to user...")
                
                # Create camera preview configuration
                camera_config = cam.create_preview_configuration()
                cam.configure(camera_config)

                # Start the camera preview (optional)
                cam.start_preview(Preview.QTGL)

                # Start the camera
                cam.start()

                # Allow time for the camera to adjust
                time.sleep(2)

                # Capture the image
                cam.capture_file(image)

                # Stop the camera
                cam.stop()

                print(f"Image captured and saved as {image}.")

                # Define email details
                sendTo = 'premsaidulla@gmail.com'  # Recipient's email
                emailSubject = "Intrusion Detected! from PIR sensor"
                emailContent = "Image received at " + time.ctime()

                # Send the email with the captured image
                sender.sendmail(sendTo, emailSubject, emailContent, image)

                # Sleep for a short duration before checking again
                time.sleep(1)

            else:
                print("No motion detected.")

        else:  # Door is CLOSED
            print("Door is CLOSED")
        
        time.sleep(1)  # Add a small delay to avoid excessive reads

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()