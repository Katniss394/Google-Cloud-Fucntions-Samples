import os
import smtplib

def tag_reader(data,context):
    email = os.environ.get('EMAIL')
    password = os.environ.get('Password')
    
   
    message ='New ticket raised'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email, 'customercare@spikeysales.com', message)
    except(smtplib.SMTPAuthenticationError e):
        print (e)


google-cloud-error-reporting
