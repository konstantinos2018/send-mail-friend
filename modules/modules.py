import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import datetime as dt

def send_mail(sender, password, receiver, msg):
    """
    Send e-mail with smtp-over-SSL/TLS mode
    ------------------------------------------------

    Args:
        sender -- string: e-mail address of sender
        password -- string: password of e-mail address of sender
        receiver -- string: e-mail address of receiver
        msg -- MIME object

    Returns:
        None
    """  
    # Send mail
    server = smtp.SMTP_SSL('smtp.gmail.com', 465)
    # server.set_debuglevel(True)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

    return None

def read_json(json_fpath):
    """
    Read json file
    ------------------------------------------------

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
    """
    Creates a MIME object using the given inputs
    ------------------------------------------------

    Args:
        subject -- string: subject of mail
        html -- string: html-formatted text acting as body of the mail
        sender -- string: e-mail address of sender
        sender_alias -- string: nickname of sender
        receiver -- string: e-mail address of receiver
        receiver_alias -- string: nickname of receiver
        
    Returns:
        msg -- MIME object
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '{0}'.format(subject)
    msg['From'] = '{0} <{1}>'.format(sender_alias, sender)
    msg['To'] = '{0} <{1}>'.format(receiver_alias, receiver)

    # construct message
    message = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
    msg.attach(message)

    return msg

def get_greetings_word(time_now):
    """
    Take a specific datetime.time() object as input and decides which greetings word
    to give as output according to if-elif rules
    ------------------------------------------------

    Args:
        time_now -- datetime.time() object

    Returns:
        greeting_word -- string: greetings word
    """
    if (time_now >= dt.time(5)) and (time_now < dt.time(12)):
        greeting_word = 'Good morning'
    elif (time_now >= dt.time(12)) and (time_now <= dt.time(17)):
        greeting_word = 'Good afternoon'
    elif (time_now > dt.time(17)) and (time_now <= dt.time(21)):
        greeting_word = 'Good evening'
    elif (time_now > dt.time(21)) or (time_now < dt.time(5)):
        greeting_word = 'Good night'

    return greeting_word