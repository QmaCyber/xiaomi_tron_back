from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

number = random.randint(1000,9999)


msg = MIMEMultipart()
 
 
message = str(number)

password = "Xxok0LKq"
msg['From'] = "xiaomitronshop@gmail.com"

msg['To'] = "im.zhaslan@gmail.com"
msg['Subject'] = "XiaomiTron - код подтверждения email"
 


msg.attach(MIMEText(message, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 


server.login(msg['From'], password)
 
 

server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 