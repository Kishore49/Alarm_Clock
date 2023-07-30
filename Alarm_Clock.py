from tkinter import *
import datetime
import time
import pygame
import os

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            print("Time to Wake up")
            try:
                pygame.mixer.init()
                audio_file = "alarm.wav"
                if os.path.exists(audio_file):
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()
                else:
                    print(f"File '{audio_file}' not found.")
            except pygame.error as e:
                print(f"Error occurred while playing audio: {e}")
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)

# Create the main window
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")

# Styling the GUI
clock.configure(bg="lightblue")

time_format = Label(clock, text="Enter time in 24-hour format!", fg="black", bg="lightblue", font=("Arial", 12, "bold"))
time_format.place(x=50, y=150)

addTime = Label(clock, text="Hour  Min Sec", font=("Arial", 14))
addTime.place(x=130)

setYourAlarm = Label(clock, text="When to wake you up:", fg="red", relief="solid", font=("Arial", 16, "bold"))
setYourAlarm.place(x=10, y=30)

# The Variables we require to set the alarm (initialization):
hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="white", width=5, font=("Arial", 12))
hourTime.place(x=110, y=70)

minTime = Entry(clock, textvariable=minute, bg="white", width=5, font=("Arial", 12))
minTime.place(x=160, y=70)

secTime = Entry(clock, textvariable=second, bg="white", width=5, font=("Arial", 12))
secTime.place(x=210, y=70)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="blue", width=10, font=("Arial", 12, "bold"), command=actual_time)
submit.place(x=140, y=120)

# Update the main loop
clock.mainloop()
