# MotoAccidentDetectionMESAHacks

## MotoCrashApp
### Overview
MotoCrashApp is a Python-based accident response simulator that automates the process of sending an emergency WhatsApp message in case of a motorcycle crash. The application allows users to enter emergency contact details, allergies, and then, after simulating a crash (or no response), sends the user's geolocation and other important information via WhatsApp. The app also displays the user's emergency contact and allergy information on the GUI after the message is sent.

### Features
- Geolocation Tracking: Uses the Google Maps Geolocation API to determine the user’s latitude and longitude.
- Automated WhatsApp Messaging: Automatically sends an emergency WhatsApp message containing the user’s contact details, allergies, and geolocation to a predefined emergency contact using pywhatkit.
- Customizable Countdown Timer: The user has 15 seconds to respond to the app before the message is sent.
GUI for User Input: Simple form to input the emergency contact name, phone number, and known allergies.
- Automatic Browser Tab Closure: The WhatsApp Web tab automatically closes after sending the message.

### Technologies
- Python 3.x
- Tkinter: For the graphical user interface.
- Google Maps Geolocation API: For retrieving geolocation data.
- Pywhatkit: For sending WhatsApp messages.
- PyAutoGUI & Keyboard: For simulating user interaction with WhatsApp Web (optional depending on use case).

### Prerequisites
- Python 3.x installed on your system.
- A Google Cloud API Key for accessing the Google Maps Geolocation API.
- pip for managing Python packages.
  
### Roadmap: Next Phases
This version of MotoCrashApp is the first phase of the project. The current phase focuses on accident response through software by sending emergency WhatsApp messages and tracking user geolocation.

### Next Phase:
- Hardware Integration: The development of the physical sensors and triggers will begin in the next phase. Specifically, we'll work on:
    - USB Trigger System: Detect when the motorcycle disconnects or crashes through a USB system connected to the motorcycle.
    - Sensor Integration: Implement sensors that can detect crash events and automatically trigger the software response.
These hardware integrations will extend the software capabilities of the current project, ensuring that emergency messages are sent automatically without requiring manual input.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
