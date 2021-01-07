import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import datetime as dt
import argparse
import sys

def send_mail(sender, password, receiver, msg):
    """
    Send e-mail with smtp-over-SSL/TLS mode
    ------------------------------------------------

    Args:
        sender (str) -- e-mail address of sender
        password (str) -- password of e-mail address of sender
        receiver (str) -- e-mail address of receiver
        msg (MIME object) -- MIME object with mail metadata

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
        json_fpath (str) -- filepath

    Returns:
        json_dict (dict) -- contains metadata e.g. email, name_alias etc
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
        subject (str) -- subject of mail
        html (str) -- html-formatted text acting as body of the mail
        sender (str) -- e-mail address of sender
        sender_alias (str) -- nickname of sender
        receiver (str) -- e-mail address of receiver
        receiver_alias (str) -- nickname of receiver

    Returns:
        msg (MIME object) -- generated MIME object that contains mail metadata
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
        time_now (datetime.time() object) -- time e.g. now or some other time user-defined

    Returns:
        greeting_word (str) -- greetings word that is used in the beginning of the e-mail's html body
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

def get_hrs_mins(time_seconds):
    """
    Converts seconds to hours and minutes
    ------------------------------------------------

    Args:
        time_seconds (int) -- numbers of seconds

    Returns:
        hrs (int) -- number of complete hours included in time_seconds
        mins (int) -- number of complete mins included in time_seconds
    """
    # compute total minutes
    time_mins_total = time_seconds / 60

    # compute hours in total minutes
    hrs = int(time_mins_total // 60)
    # compute remaining minutes in total minutes
    mins = int(time_mins_total % 60)

    return hrs, mins

def extract_opts():
    """
    Extracts the options of the script that the functions is running
    ------------------------------------------------

    Args:
        None
    Returns:
        args (dict) -- keys=command-line option, values=True/False/list of arguments
    """
    
    # Create parser object
    parser = argparse.ArgumentParser(description='Send e-mail in interactive and non interactive mode.')

    # Add --interactive option
    parser.add_argument('-i', '--interactive-date', action='store_true', help='Runs script in interactive mode,\
        i.e. explicitly asks user for input', required=False)

    # Add --mail option with e-mail address and name alias arguments
    parser.add_argument('-m', '--mail', action='store', nargs=2, metavar='', help='Insert e-mail address of sender and name alias,\
        e.g. mail@domain.xxx "Manos Danezis"', required=False)

    # Convert to dictionary
    args = vars(parser.parse_args())
    
    return args