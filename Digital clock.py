import tkinter
from time import strftime
Timex = tkinter.Tk() #root
Timex.title("Digital Clock")

set_window = tkinter.Label(Timex, font=("DS-Digital", 100), #label
                           background="black", foreground="cyan")
set_window.pack(anchor="center")


def time():
    patt = strftime("%I:%M:%S %p")
    set_window.config(text=patt)
    set_window.after(1000, time)


time()
tkinter.mainloop()



# #to get email's list from a huge data----------------------------------------------
# # email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
# # email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",str)
# print(re.findall(r'\w+@\S+\w',str))

# #dice simulator---------------------------------------------------------
# from tkinter import Tk, Label, Button
# from random import choice
# root = Tk()
# root.title("Role Dice")
# root.geometry("500x500")
# label = Label(root, font=("helvetica", 250, "bold"))


# def rolldice():
#     dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
#     label.config(text=choice(dice))
#     label.pack() #we also can pack it outside of the function


# button = Button(root, font=("helvatica", 20, "bold"),
#                 text="click here", command=rolldice)
# button.pack()
# root.mainloop()

# check a number is perfect or not-------------------------------------------
# x= int(input("enter the number :"))
# sum=0
# for i in range(1,x):
#     if x%i==0:
#         sum+=i
# if sum==x:
#     print(x," is a perfect number.")
# else:
#     print(x," is not a perfect number.")        


# # fulfilment messege on whatsapp----------------------------------------------
# import pywhatkit as kit
# import datetime

# # Phone number (include country code without '+')
# phone_number = "+918240248311"

# # Message to send
# message = "Hello from Python!"

# # Get the current time
# now = datetime.datetime.now()

# # Specify the time to send the message (hour, minute)
# send_time = (now.hour, now.minute + 1)  # Send after 1 minute from current time

# # Send the message
# kit.sendwhatmsg(phone_number, message, send_time[0], send_time[1])