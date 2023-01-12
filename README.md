# BulkEmailer
usage: eBulker.py [-h] [-a ATTACH] -c CONTACTS -b BODY -s SUBJECT

BEFORE USE:
You must enter your own email and email password in the script. You may also need to change the SMTP server and port.

Contacts File:
Your contacts file should be stored as a .csv file. The first line should contain "name,email" as headers (as this line is skipped)

eg:
name,email
spud,test@fakemail.com

Attachement File:
Aware of an issue in the CLI version where the attachment name is set to the full file path. Working on this. Also working on a version where an attachment is not necessary. 

Subject:
This is the subject of the email you are sending.

Body File:
This is a text file containing the body of the email
