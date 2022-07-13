#Prerequisites:
#The body of you email 
#
#

#Import dependencies
import smtplib 
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#Declare variables
fromaddr = 'EMAILADDRESS'
pword = 'EMAILPASSWORD'
filename = 'PATH/TO/ATTACHMENT/FILENAME'
contactsPath = 'PATH/TO/CONTACTS.csv'
emailBodyPath = 'PATH/TO/EMAIL/BODY.txt'

#Create server connection
server = smtplib.SMTP('smtp.office365.com', 587)
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
            msg['Subject'] = 'Multi Factor Authentication'
            body = f'Dear {name}, \n' + tempBody
            msg.attach(part)
            msg.attach(MIMEText(body, 'plain'))
            server.sendmail(fromaddr, toaddr, msg.as_string())

server.quit()