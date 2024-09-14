import tkinter as tk
from tkinter import messagebox
import threading
import time
import webbrowser

class AccidentResponseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accident Response Simulator")
        self.timer = 8  # Time to respond (8 seconds)
        self.response_received = False

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
        while self.timer > 0:
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

    # Sends an alert (simulated using a web link to a map)
    def send_alert_to_responders(self):
        messagebox.showwarning("No Response", "Sending alert to emergency responders!")
        # Simulate sending a signal to responders
        webbrowser.open("https://www.google.com/maps/search/hospitals+near+me/")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AccidentResponseApp(root)
    root.mainloop()
