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
GOOGLE_API_KEY = "API_KEY"

class AccidentResponseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MotoCrashApp")
        self.timer = 5  # Time to respond (5 seconds)
        self.response_received = False

        # Emergency contact details entry fields
        appName = tk.Label(root, text="MotoCrashApp", font=("Courier 22 bold"))
        appName.grid(row=0, column=1)

        eName = tk.Label(root, text="Enter emergency contact name: ", font=("Courier 15 bold"))
        eName.grid(row=1, column=0, pady=10)
        self.emergency_name = tk.Entry(root)
        self.emergency_name.grid(row=1, column=1)

        eNum = tk.Label(root, text="Enter emergency contact number: ", font=("Courier 15 bold"))
        eNum.grid(row=2, column=0, pady=10)
        self.emergency_number = tk.Entry(root)
        self.emergency_number.grid(row=2, column=1)

        eTxt = tk.Label(root, text="What allergies do you have: ", font=("Courier 15 bold"))
        eTxt.grid(row=3, column=0, pady=10)
        self.allergies = tk.Entry(root)
        self.allergies.grid(row=3, column=1)

        # Start button to start the timer
        self.start_button = tk.Button(root, text="Start", command=self.start_process, width=10)
        self.start_button.grid(row=4, column=1, pady=20)

        # Yes and No buttons for user response (hidden initially)
        self.yes_button = tk.Button(root, text="Yes", command=self.yes_response, width=10)
        self.no_button = tk.Button(root, text="No", command=self.no_response, width=10)

        # Timer label (hidden initially)
        self.timer_label = tk.Label(root, text=f"Respond within: {self.timer} seconds", font=("Arial", 14))

    # Method triggered when the Start button is clicked
    def start_process(self):
        # Show Yes and No buttons after clicking Start
        self.yes_button.grid(row=5, column=0, pady=20)
        self.no_button.grid(row=5, column=1, pady=20)

        # Show the timer label and start the countdown
        self.timer_label.grid(row=6, column=1, pady=20)
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

        # Timer reached 0, send alert automatically if no response is received
        if not self.response_received:
            # Ensure emergency details are collected when no response is given
            self.get_emergency_details()
            self.send_alert_to_responders()

    # If user clicks Yes
    def yes_response(self):
        self.response_received = True
        messagebox.showinfo("Response", "Glad you're okay. No alert sent.")
        self.root.destroy()

    # If user clicks No
    def no_response(self):
        self.response_received = True
        self.get_emergency_details()  # Get user input before sending alert
        self.send_alert_to_responders()

    # Collect emergency contact details
    def get_emergency_details(self):
        self.name = self.emergency_name.get()
        self.number = self.emergency_number.get()
        self.allergy_info = self.allergies.get()

    # Sends an alert (simulated WhatsApp message to emergency contact)
    def send_alert_to_responders(self):
        # Collect user input
        contact_name = self.name
        contact_number = self.number
        allergies = self.allergy_info

        # Get geolocation and send WhatsApp message with additional details
        self.get_geolocation(contact_name, contact_number, allergies)

    # Get geolocation using Google Maps Geolocation API and send WhatsApp message
    def get_geolocation(self, contact_name, contact_number, allergies):
        try:
            # URL for the Google Geolocation API
            url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + GOOGLE_API_KEY

            # Send a POST request to the API
            response = requests.post(url, json={})
            location_data = response.json()

            # Extract latitude and longitude
            latitude = location_data['location']['lat']
            longitude = location_data['location']['lng']

            # Prepare the WhatsApp message with geolocation and user details
            full_message = (f"Accident detected. Emergency Contact: {contact_name}, "
                            f"Phone: {contact_number}, Allergies: {allergies}. "
                            f"Call ambulance to this location: Latitude: {latitude}, Longitude: {longitude}")

            # Get current time for sending the message in the next minute
            now = datetime.datetime.now()
            time_hour = now.hour
            time_minute = now.minute + 1

            if time_minute == 60:
                time_minute = 0
                time_hour += 1

            # Parameters for WhatsApp auto send
            waiting_time_to_send = 8  # Wait 8 seconds to send the message
            close_tab = True  # Close the tab after sending
            waiting_time_to_close = 2  # Wait 2 seconds before closing the tab

            # Send the message with automatic options
            pywhatkit.sendwhatmsg(contact_number, full_message, time_hour, time_minute, 
                                  waiting_time_to_send, close_tab, waiting_time_to_close)
            
            # # Add delay to ensure whatsapp web page is fully loaded
            # time.sleep(15) # adjust value base on time it takes for page to load

            # #simulate the press enter
            # pyautogui.press('enter')

            # Show user info in a new window after sending the message
            self.show_user_info()

        except Exception as e:
            messagebox.showerror("Error", f"Unable to get geolocation or send WhatsApp message: {e}")

    # Display user information in a new window
    def show_user_info(self):
        user_info_window = tk.Toplevel(self.root)
        user_info_window.title("User Information")

        # Display the user's details in the new window
        name_label = tk.Label(user_info_window, text=f"Name: {self.name}", font=("Arial", 14))
        name_label.pack(pady=10)

        allergies_label = tk.Label(user_info_window, text=f"ALLERGIES: {self.allergy_info}", font=("Arial", 14))
        allergies_label.pack(pady=10)

        contact_label = tk.Label(user_info_window, text=f"Emergency Contact: {self.name}", font=("Arial", 14))
        contact_label.pack(pady=10)

        phone_label = tk.Label(user_info_window, text=f"Emergency Number: {self.number}", font=("Arial", 14))
        phone_label.pack(pady=10)

        close_button = tk.Button(user_info_window, text="Close", command=user_info_window.destroy)
        close_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AccidentResponseApp(root)
    root.mainloop()