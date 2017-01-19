import smtplib

gmail_user = 'stanickjamino@gmail.com'  
gmail_password = 'SANTHOMEPK'

try:  
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.starttls()
    
    server.login(gmail_user, gmail_password)
except:  
    print 'Something went wrong...'
humanHardDrive@gmail.com
