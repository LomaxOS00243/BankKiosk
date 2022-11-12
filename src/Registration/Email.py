#function that sends code to user email
def send_content_to_email(email, emailContent):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    #create email message
    msg = MIMEMultipart()
    msg['From'] = 'azureTeamKiosk@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Your Credentials'
    body = 'Your credentials is: ' + emailContent
    msg.attach(MIMEText(body, 'plain'))
    #create email server
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login('azureTeamKiosk@gmail.com', 'ccpxlerobzrpkjum')
    #send email
    try:
        email_server.sendmail('adad', email, msg.as_string())
        email_server.quit()
        return True
    except:
        return False
