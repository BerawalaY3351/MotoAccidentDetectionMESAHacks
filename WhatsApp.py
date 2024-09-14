import pywhatkit
import datetime
import time #might not be necessary
import pyautogui
import keyboard



# Variables
phone_number = '‭+14082282128‬'
group_id = ''
message = 'Accident detected. Call ambulance to this location: '

now = datetime.datetime.now()

current_hour = now.hour
current_minute = now.minute + 1

if current_minute == 60:
    current_minute = 0
    current_hour += 1
    if current_hour == 24:
        current_hour = 0

hour_str = str(current_hour)


time_hour = current_hour
time_minute = current_minute
waiting_time_to_send = 8
close_tab = True
waiting_time_to_close = 2

mode = "contact"

if mode == "contact":
    # Send a WhastApp message to an specific contact
    pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)


    pyautogui.click(3024, 1964)
    #time.sleep(0.1)
    keyboard.press_and_release('enter')


elif mode == "group":
    # Send a WhastApp message to an specific group
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)



else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")
