import smtplib
from email.mime.text import MIMEText
import getpass


myAddress = input("Podaj adres email: ")
my_password = getpass.getpass('podaj haslo do poczty: ')
subject = input("Podaj temat wiadomosci: ")
content = input("Podaj treść wiadomości: \n")

def alertMe(subject, body):
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = myAddress
    msg['Reply-to'] = myAddress
    msg['To'] = myAddress


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(myAddress, my_password)
    server.sendmail(myAddress,myAddress,msg.as_string())
    server.quit()

alertMe(subject, content)

