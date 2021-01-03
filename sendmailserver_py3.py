#!/usr/bin/env python
# -*- coding: utf-8 -*-
# === IMPORTS ===
import datetime as dt
from modules import modules

# Message 
# Read sensitive data JSON file
sens_data = modules.read_json('./sensitive_data.json')

sender = sens_data['Sender'][0]['mail']
password = sens_data['Sender'][0]['password']
receiver = sens_data['Receiver'][0]['mail']

# Define intro word
t = dt.datetime.now()

if (t.hour >= 5) and (t.hour < 12):
  in_word = 'Good morning'
elif (t.hour >= 12) and (t.hour <= 17):
  in_word = 'Good afternoon'
elif (t.hour > 17) and (t.hour <= 21):
  in_word = 'Good evening'
elif (t.hour > 21) and (t.hour < 5 ):
  in_word = 'Good night'

# Compute time period until leave
t_leave = dt.datetime(2020, 10, 23, 15, 15, 0, 0) # leaving time
t_diff = t_leave - t

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
""".format(in_word, t_diff_mins)

subject = 'Χωρίς Θέμα'
sender_alias = 'Άγνωστος'
receiver_alias = 'Άγνωστος'

# create MIME object
msg = modules.create_MIME(subject=subject, html=html, sender=sender, sender_alias=sender_alias, receiver=receiver, receiver_alias=receiver_alias)

# Send mail
modules.send_mail(sender, password, receiver, msg)

