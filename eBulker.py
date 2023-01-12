#Prerequisites:
#The body of your email in a txt file
#The contacts to send the email to as a csv file with name and toaddr fields
#An attachment - You may need to change the MIMEBase maintype

#Import dependencies
import smtplib 
import csv
import tkinter as win;
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#Create the GUI
root = win.Tk()
root.title('Create Bulk Email')
canvas = win.Canvas(root,width=500,height= 500, relief= 'raised',bg= '#646262')
canvas.pack()
title = win.Label(root,text='Create your bulk email',font=('serif', 20),bg= '#646262', fg='white')
canvas.create_window(250,30,window=title)

#Ask user to enter email address and password for email
labelFromAddr = win.Label(root,text='Enter your email address:',font=('serif',12),bg= '#646262', fg='white')
canvas.create_window(100,70,window=labelFromAddr)
frommAddrString = win.Entry(root,width=50,border=2,)
canvas.create_window(160,100,window=frommAddrString)
labelPword = win.Label(root,text='Enter your email password:',font=('serif',12),bg= '#646262', fg='white')
canvas.create_window(100, 130, window=labelPword)
pwordString = win.Entry(root,width= 50, border = 2, show='*')
canvas.create_window(160,150, window=pwordString)

def login():
    fromaddr = frommAddrString.get()
    pword = pwordString.get()
    # #Create server connection
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, pword)
    labelSuccess = win.Label(root, text='Login success!', font=('serif', 14), bg= '#646262', fg='white')
    canvas.create_window(200, 230, window = labelSuccess)
    buttonLogin.config(state='disabled')
    
buttonLogin = win.Button(root,text = 'Login', font=('serif',12),command=login)
canvas.create_window(200, 200, window= buttonLogin)

# #Declare variables
# fromaddr = 'EMAIL'
# pword = 'PASSWORD'
# filename = 'PATH/TO/ATTACHMENT'
# contactsPath = 'PATH/TO/CONTACTS.csv'
# emailBodyPath = 'PATH/TO/EMAIL/BODY.txt'



# #read the csv file line by line
# with open(contactsPath) as contacts:
#     reader = csv.reader(contacts)
#     next(reader)

#     #create a 'part' of the email containing an attachment
#     with open(filename, 'rb') as file:
#         part = MIMEBase("application", "octet-stream")
#         part.set_payload(file.read())
#         file.close()

#     #encode and add headers for the email to be sent
#     encoders.encode_base64(part)
#     part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}")

#     #personalise the body of the email
#     with open(emailBodyPath) as content:
#         tempBody = content.read()
#         content.close()

#         #for every name and address in the csv file craft a new email with personalised body and same attachment as above
#         for name, toaddr in reader:
#             msg = MIMEMultipart()
#             msg['From'] = fromaddr
#             msg['Subject'] = 'Multi Factor Authentication'
#             body = f'Dear {name}, \n' + tempBody
#             msg.attach(part)
#             msg.attach(MIMEText(body, 'plain'))
#             server.sendmail(fromaddr, toaddr, msg.as_string())

# server.quit()
root.mainloop()