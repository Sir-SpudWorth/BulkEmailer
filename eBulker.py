#Prerequisites:
#The body of your email in a txt file
#The contacts to send the email to as a csv file with name and toaddr fields
#An attachment - You may need to change the MIMEBase maintype

#Import dependencies
import smtplib 
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import argparse

#Initialise parser
parser = argparse.ArgumentParser(description='Send bulk emails')

#Add arguments
parser.add_argument('-a', '--attach', help='Filepath of the attachment')
parser.add_argument('-c', '--contacts', required=True, help='Filepath to Contacts.csv file')
parser.add_argument('-b', '--body', required=True, help='Filepath to email body.txt')
parser.add_argument('-s', '--subject', required=True, help='The subject of the email')

# Extract arguments into variable
args = parser.parse_args()

#Declare variables
fromaddr = 'EMAIL' # CHANGE THIS
pword = 'PASSWORD' # CHANGE THIS
filename = args.attach
contactsPath = args.contacts
emailBodyPath = args.body

#Create server connection
server = smtplib.SMTP('smtp.office365.com', 587) # CHANGE THIS
server.ehlo()
server.starttls()
server.login(fromaddr, pword)

#read the csv file line by line
with open(contactsPath) as contacts:
    reader = csv.reader(contacts)
    next(reader)

    #create a 'part' of the email containing an attachment
    with open(filename, 'rb') as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())
        file.close()

    #encode and add headers for the email to be sent
    encoders.encode_base64(part)
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}")

    #personalise the body of the email
    with open(emailBodyPath) as content:
        tempBody = content.read()
        content.close()

        #for every name and address in the csv file craft a new email with personalised body and same attachment as above
        for name, toaddr in reader:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['Subject'] = args.subject
            body = f'Dear {name}, \n' + tempBody
            msg.attach(part)
            msg.attach(MIMEText(body, 'plain'))
            server.sendmail(fromaddr, toaddr, msg.as_string())

server.quit()