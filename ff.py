import imaplib, serial, struct, time
import imaplib, email
import sys
import time
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from datetime import datetime
import randfacts
import cv2

def sendwebcam(q):
    fromaddr = "Yashlaptop07@gmail.com"
    toaddr = q
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Webcam Picture taken at"+str(datetime.now())
    
    # string to store the body of the mail 
    body = "Thanks for contacting yashs pc here is a random fact for you : \n"+randfacts.getFact(False)
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "Webcam.png"
    attachment = open("D:\STUDY\Experimental shit\LaptopGmail\Webcam.png", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, "Yash7150") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 

















while True :
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (typ, capabilities) =mail.login('Yashlaptop07@gmail.com', 'Yash7150')
    mail.list()
    mail.select('inbox')

    #need to add some stuff in here
    (typ, data) = mail.search(None, '(UNSEEN)')
    if(data[0]!=b""):
        print("run")
        ids = data[0]
        id_list = ids.split()
        #get the most recent email id
        latest_email_id = int( id_list[-1] )

        #iterate through 15 messages in decending order starting with latest_email_id
        #the '-1' dictates reverse looping order
        for i in range( latest_email_id, latest_email_id-1, -1 ):
            typ, data = mail.fetch( str(i), '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                varSubject = msg['subject']
                varFrom = msg['from']

        #remove the brackets around the sender email address
        varFrom = varFrom.replace('<', '')
        varFrom = varFrom.replace('>', '')

        #add ellipsis (...) if subject length is greater than 35 characters
        if len( varSubject ) > 35:
            varSubject = varSubject[0:32] + '...'

        emailid= varFrom.split()[-1] 
        subject= varSubject
        print(subject)
        print(emailid)

        password=varSubject.split()[0]
        print(password)
        Action=varSubject.split()[1]
        print(Action)
        if (password=="blipblip"):
            possibleactions=["Shutdown","Restart","Sleep","OpenNetflix","SendStatus","ClickWebcampicture"]
            option=possibleactions.index(Action)
            if(option==0):
                os.system("shutdown /p")
                sys.exit()
            if(option==5):
                camera = cv2.VideoCapture(0)
                for i in range(1):
                    return_value, image = camera.read()
                    cv2.imwrite('Webcam.png', image)
                del(camera)           
                sendwebcam(emailid)
                time.sleep(45)
            time.sleep(40)
        else:
            time.sleep(40)
    else:
        print("didnotrun")
        time.sleep(45)


    
