#Hopefully simplified version
import smtplib 
import csv
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import ctypes
user32 = ctypes.windll.user32
screensizex = user32.GetSystemMetrics(0)
screensizey = user32.GetSystemMetrics(1)

print(screensizex, screensizey)
#Create the window
window = Tk()
window.title("Bulk Emailer")
window.geometry(str(screensizex) + 'x' + str(screensizey))
window.configure(background= "white")


emailVar = StringVar()
passVar = StringVar()
email = Label(window,text= "Enter your email address: ", font=("serif", 14)).grid(row=0,column=0)
password = Label(window, text = "Enter your email password: ", font=("serif", 14)).grid(row=1,column=0)
emailEntry = Entry(window, textvariable= emailVar).grid(row = 0, column= 1)
passEntry = Entry(window, show="*", textvariable= passVar).grid(row = 1, column= 1)

l = StringVar()
loginCheck = Label(window, textvariable= l, font=("serif", 14), text= "").grid(row= 2, column=1, padx = 2)
def login():
    #Gets the strings entered in the text boxes and assigns them to variables
  
    fromaddr = emailVar.get()
    pword = passVar.get()
    #Create server connection
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    #Tries to authenticate the SMTP using the login details provided
    try:
        server.login(fromaddr, pword)
        l.set("Login Successful!")
    except smtplib.SMTPAuthenticationError:
        l.set("Login Unsuccessful - Wrong email/password")

emailButton = Button(window, text = "Login", command=login, font=("serif", 14)).grid(row = 2, column=0)

contacts = Label(window, text= "Select the contacts you wish to send to (.CSV):", font=("serif", 14)).grid(row=4, column = 0)

def open_contacts():
    #Opens the file explorer to allow the user to select the file they want
    contacts = filedialog.askopenfile(mode='r', filetypes=[('Comma Separated Values Files','*.csv')])
    if contacts:
        filename = contacts.name
        filename= os.path.basename(filename)
        content = contacts.readlines()
        fileChosen = Label(window,text= "'" + filename + "'", font=("serif",14)).grid(row=5,column = 0)
        
contactsButton = Button(window,text = "Browse", command=open_contacts, font=("serif", 14)).grid(row=4,column=1)



window.mainloop()