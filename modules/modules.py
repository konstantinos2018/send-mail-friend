import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def send_mail(sender, password, receiver, msg):
      
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
        json_dict -- dictionary
    """

    with open(json_fpath, mode='r') as json_file:
        json_str = json_file.read()
        json_dict = json.loads(json_str)
    return json_dict

def create_MIME(subject='', html='', sender='', sender_alias='Incognito', receiver='', receiver_alias='Incognito'):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '{0}'.format(subject)
    msg['From'] = '{0} <{1}>'.format(sender_alias, sender)
    msg['To'] = '{0} <{1}>'.format(receiver_alias, receiver)

    # construct message
    message = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
    msg.attach(message)

    return msg