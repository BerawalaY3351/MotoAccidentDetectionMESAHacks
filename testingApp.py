from tkinter import *
import tkinter as tk


my_entries = []

def display_text():
    global entry
    string = entry.get()
    label.configure(text=string)

def create_window():
    new_window = Tk()
    new_window.geometry("750x250")
 
def something():
    entry_list = ''
    
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_label.config(text=entry_list + '\n')
        
    print(my_entries[3].get())

    create_window()

old_window = Tk()
old_window.geometry("3024x1964")

appName=Label(old_window, text="MotoCrashApp", font=("Courier 22 bold"))
appName.grid(row = 0, column = 1)

eName=Label(old_window, text="Enter emergency contact name: ", font=("Courier 15 bold"))
eName.grid(row = 1, column = 1)

eNum=Label(old_window, text="Enter emergency contact number: ", font=("Courier 15 bold"))
eNum.grid(row = 2, column = 1)

eTxt = Label(old_window, text = "Enter Emergency text msg: ", font = ("Courier 15 bold"))
eTxt.grid(row = 3, column = 1)

for x in range(3):
    my_entry = Entry(old_window, width = 25)
    my_entry.grid(row = x + 1, column = 5, pady = 5, padx = 5)
    my_entries.append(my_entry)


acceptBut = Button(old_window, text = "Enter", command = something)
acceptBut.grid(row = 5, column = 5, pady = 20)

my_label = Label(old_window, text = '')
my_label.grid(row=5, column = 2, pady=20)

old_window.mainloop()
