import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_senden(empfänger,text): #function that sends a mail from the mail account you 
                                  # put into the mail variable
    email = "your.mail@gmx.de"
    password = "yourpasswort"
    empfaenger = empfänger
    betreff = "Täglicher Wetterbericht"
    inhalt = text
    msg = MIMEText(inhalt)
    msg["From"] = email
    msg["To"] = empfaenger
    msg["Subject"] = betreff

    try:
        with smtplib.SMTP_SSL("mail.gmx.net", 465) as server:
            server.login(email, password)
            server.sendmail(email, empfaenger, msg.as_string())
            print("E-Mail erfolgreich gesendet!")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")
