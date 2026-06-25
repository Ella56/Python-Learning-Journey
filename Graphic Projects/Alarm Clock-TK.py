#imports and global variables

import tkinter as tk
from datetime import datetime
from tkinter import messagebox


window = tk.Tk()
window.title("Alarm Clock App")
window.resizable(width=False, height=False)
window.geometry("400x300")




#function for getting current time

def get_current_time():
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    compare_alarm_with_current_time(current_time)
    window.after(1000, get_current_time)




#function to set alarm timer
def set_alarm():
    global alarm_time
    current_time = datetime.now()
    alarm_time = current_time.replace(hour=int(hour_alarm_entry.get()), minute=int(minute_alarm_entry.get()), second=0, microsecond=0)
    latest_alarm_label.configure(text = alarm_time.strftime("%H:%M:%S"))




#function for comparing time with alarm

def compare_alarm_with_current_time(current_time):
    global alarm_time
    if alarm_time is not None and current_time >= alarm_time:
        messagebox.showinfo("showinfo", "Your alarm has happened")
        latest_alarm_label.configure(text='No alarm has been set')
        alarm_time = None





#UI design

time_label = tk.Label(window, text='12:30:30', font=("Tahoma",32))
time_label.pack()



tk.Label(window, text="Hour").pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()

tk.Label(window, text="Minute").pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()


tk.Button(window, text="Set Alarm", command=set_alarm).pack()

latest_alarm_label = tk.Label(window, text="No alarm has been set")
latest_alarm_label.pack()





#running application
get_current_time()
window.mainloop()


