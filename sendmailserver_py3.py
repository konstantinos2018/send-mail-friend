#!/usr/bin/env python
# -*- coding: utf-8 -*-
# === IMPORTS ===
import datetime as dt
from modules import modules
import os

# Message 
# Read sensitive data JSON file
sens_data = modules.read_json(os.path.join(os.path.abspath(__file__), '../sensitive_data.json'))

sender = sens_data['Sender'][0]['mail']
password = sens_data['Sender'][0]['password']
receiver = sens_data['Receiver'][0]['mail']

# Define intro word
t_now = dt.datetime.now()
greeting_word = modules.get_greetings_word(t_now.time())

# Compute time period until leave
t_leave = dt.datetime(2020, 10, 23, 15, 15, 0, 0) # leaving time
t_diff = t_leave - t_now

# convert time to minutes
t_diff_mins = t_diff.total_seconds() / 60


# Create message content and metadata
html = """\
<html>
  <head></head>
  <body>
    <p>{0},</p>
    <p>
	   {1} minutes remaining
    </p>
    <p>Kind Regards,<br>
    Kostas</p>
  </body>
</html>
""".format(greeting_word, t_diff_mins)

subject = 'Greetings'
sender_alias = sens_data['Sender'][0]['name_alias']
receiver_alias = sens_data['Receiver'][0]['name_alias']

# create MIME object
msg = modules.create_MIME(subject=subject, html=html, sender=sender, sender_alias=sender_alias, receiver=receiver, receiver_alias=receiver_alias)

# Send mail
modules.send_mail(sender, password, receiver, msg)

