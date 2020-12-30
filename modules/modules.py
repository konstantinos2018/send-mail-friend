import smtplib as smtp
from email.mime.text import MIMEText
import json

def send_mail(sender, password, receiver, html, msg):
    
    # construct message
    message = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
    msg.attach(message)
    
    # Send mail
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

    return None

def read_json(json_fpath):
    """Read json file
    Args:
        json_fpath -- string (filepath)
    Returns:
        json_dict -- list
    """

    with open(json_fpath, mode='r') as json_file:
        json_str = json_file.read()
        json_dict = json.loads(json_str)
    return json_dict