# Let's integrate the logic from WhatsApp.py into the existing accident response app

import tkinter as tk
from tkinter import messagebox
import threading
import time
import requests
import pywhatkit
import datetime
import pyautogui
import keyboard

# Replace 'YOUR_GOOGLE_API_KEY' with your actual Google API key
GOOGLE_API_KEY = "AIzaSyD48OWXJDHBghssUfppGvtfrQPqtNrn_9Q"

# Variables for WhatsApp integration
phone_number = '+14082282128'  # Add the desired phone number
message = 'Accident detected. Call ambulance to this location: '

class AccidentResponseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accident Response Simulator")
        self.timer = 15  # Time to respond (15 seconds)
        self.response_received = False
        self.stop_timer = False  # Flag to stop timer thread

        # Label asking the user if they are okay
        self.label = tk.Label(root, text="Are you okay?", font=("Arial", 18))
        self.label.pack(pady=20)

        # Yes and No buttons for user response
        self.yes_button = tk.Button(root, text="Yes", command=self.yes_response, width=10)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(root, text="No", command=self.no_response, width=10)
        self.no_button.pack(side=tk.RIGHT, padx=20)

        # Timer label to show countdown
        self.timer_label = tk.Label(root, text=f"Respond within: {self.timer} seconds", font=("Arial", 14))
        self.timer_label.pack(pady=20)

        # Start the countdown timer
        self.start_timer()

    # Method to start the timer
    def start_timer(self):
        self.thread = threading.Thread(target=self.countdown)
        self.thread.start()

    # Countdown timer
    def countdown(self):
        while self.timer > 0 and not self.response_received:
            time.sleep(1)
            self.timer -= 1
            self.timer_label.config(text=f"Respond within: {self.timer} seconds")
            if self.response_received:
                return
        # If no response is received, send an alert
        self.send_alert_to_responders()

    # If user clicks Yes
    def yes_response(self):
        self.response_received = True
        messagebox.showinfo("Response", "Glad you're okay. No alert sent.")
        self.root.destroy()

    # If user clicks No
    def no_response(self):
        self.response_received = True
        self.send_alert_to_responders()
        self.get_geolocation()

    # Sends an alert (simulated SMS message or phone call to emergency responders)
    def send_alert_to_responders(self):
        messagebox.showwarning("No Response", "Accident detected. Sending message to emergency responders!")
    
    # Get geolocation using Google Maps Geolocation API and send WhatsApp message
    def get_geolocation(self):
        try:
            # URL for the Google Geolocation API
            url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + GOOGLE_API_KEY

            # Send a POST request to the API
            response = requests.post(url, json={})
            location_data = response.json()

            # Extract latitude and longitude
            latitude = location_data['location']['lat']
            longitude = location_data['location']['lng']

            # Prepare the message with geolocation
            full_message = f"{message} Latitude: {latitude}, Longitude: {longitude}"

            # WhatsApp integration: calculate the time for message sending
            now = datetime.datetime.now()
            time_hour = now.hour
            time_minute = now.minute + 1

            if time_minute == 60:
                time_minute = 0
                time_hour += 1
                if time_hour == 24:
                    time_hour = 0

            # Send a WhatsApp message with the geolocation data
            pywhatkit.sendwhatmsg(phone_number, full_message, time_hour, time_minute, 10, True, 2)
            pyautogui.click(3024, 1964)  # Adjust coordinates for click
            keyboard.press_and_release('enter')

            # Inform the user that the message has been sent
            messagebox.showinfo("WhatsApp", "Geolocation sent via WhatsApp!")

        except Exception as e:
            messagebox.showerror("Error", f"Unable to get geolocation or send WhatsApp message: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccidentResponseApp(root)
    root.mainloop()

