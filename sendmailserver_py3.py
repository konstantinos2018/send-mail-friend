#!/c/Anaconda3/envs/myenv/python

# === IMPORTS ===
import datetime as dt
from modules import modules
import os, sys

# Extract command-line arguments
args = modules.extract_opts()

if args['interactive_date']:
  t_lockdown = input('Lockdown date must be in the following format d-m-yyyy.\nInsert date here: \n')
  t_lockdown = dt.datetime.strptime(t_lockdown, '%d-%m-%Y')
  
else:
  t_lockdown = dt.datetime(2021, 1, 11, 6, 0, 0, 0) # Lockdown finishing

# Define intro word
t_now = dt.datetime.now()
greeting_word = modules.get_greetings_word(t_now.time())

# Compute time period until getting out of lockdown
t_diff = t_lockdown - t_now

# convert time to minutes
# t_diff_mins = t_diff.total_seconds() / 60
t_diff_hrs, t_diff_mins = modules.get_hrs_mins(t_diff.seconds)

# Create message content and metadata
html = """\
<html>
  <head></head>
  <body>
    <p>{0} &#128516;,</p>
    <p>
      {1} days {2} hrs and {3} mins remaining until lockdown ends...
    </p>
    <p>
      or {4:.0f} minutes...
    </p>
    <p>
      or {5:.0f} seconds
    </p>
    <p>Kind Regards,<br>
    Kostas</p>
  </body>
</html>
""".format(greeting_word, t_diff.days, t_diff_hrs, t_diff_mins, t_diff.total_seconds()/60, t_diff.total_seconds())

# Read sensitive data JSON file
# sens_data = modules.read_json(os.path.join(os.path.abspath(__file__), '../sensitive_data.json'))
sens_data = modules.read_json('./sensitive_data.json')
# Assign values to mail metadata variables
sender = sens_data['Sender'][0]['mail']
password = sens_data['Sender'][0]['password']
if args['mail']:
  receiver = args['mail'][0]
  receiver_alias = args['mail'][1]
else:
  receiver = sens_data['Receiver'][2]['mail']
  receiver_alias = sens_data['Receiver'][2]['name_alias']

subject = 'Greetings'
sender_alias = sens_data['Sender'][0]['name_alias']


# create MIME object
msg = modules.create_MIME(subject=subject, html=html, sender=sender, sender_alias=sender_alias, receiver=receiver, receiver_alias=receiver_alias)

# Send mail
modules.send_mail(sender, password, receiver, msg)

