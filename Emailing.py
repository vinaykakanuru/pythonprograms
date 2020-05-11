# You need to give less secure apps confirmation before using gmail in SMTP
# or enable google 2 step verification and
# create google app password instead using gmail password
import smtplib

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('XXXXX@gmail.com','password')
    subject = 'Test Mail'
    body = 'Hey Vinay,\n\nThis is test mail.\n\nRegards,\nVinay'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('XXXXXX@gmail.com', 'YYYYYY@gmail.com', msg)
    print("Email Sent")

sendMail()
