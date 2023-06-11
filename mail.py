import smtplib,email 
from email.message import EmailMessage
msg = EmailMessage()
msg.set_content("ALERT!!! motion detected in the frame!")
with open("home1.jpg", "rb") as fp:
    msg.add_attachment(fp.read(), maintype="image", subtype="jpg")
    msg['subject'] = "Security Alter human detected detected!"
    #msg['to'] = "rajskams@gmail.com"
    msg['to'] = "gokulappadurai.k@ckcet.ac.in"
    user = "k.gokulappaduraikjgv@gmail.com"
    msg['from'] = user
    password = "pomymwwvzvxvarrt"
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
                    
