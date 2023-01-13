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

#Create the window
window = Tk()
window.title("Bulk Emailer")
window.geometry('600x600')
window.configure(background= "white")


emailVar = StringVar()
passVar = StringVar()
email = Label(window,text= "Enter your email address: ", font=("serif", 14)).grid(row=0,column=0)
password = Label(window, text = "Enter your email password: ", font=("serif", 14)).grid(row=1,column=0)
emailEntry = Entry(window, textvariable= emailVar).grid(row = 0, column= 1)
passEntry = Entry(window, show="*", textvariable= passVar).grid(row = 1, column= 1)

def login():
    #Gets the strings entered in the text boxes and assigns them to variables
    fromaddr = emailVar.get()
    pword = passVar.get()
    #Create server connection
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    #Tries to authenticate the SMTP using the login details provided
    server.login(fromaddr, pword)
    loginSuccess = Label(window, text = "Login Successful!", font=("serif", 14)).grid(row = 2, column=1)

emailButton = Button(window, text = "Login", command=login, font=("serif", 14)).grid(row = 2, column=0)





window.mainloop()