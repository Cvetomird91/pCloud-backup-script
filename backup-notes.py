#!/usr/bin/env python3

import os
import datetime
import pathlib
import re
import sys, traceback

user_home = os.getenv("HOME")
drive_dir = '/pCloudDrive/'
drive_path = user_home + drive_dir
notes_path = drive_path + 'notes/'

notes = os.listdir(notes_path)
files = os.listdir(drive_path)
available_backups = []

date = datetime.datetime.now()
current_date = date.strftime('%d.%m.%Y')
new_dir = 'notes-' + current_date

for file in files:
    matchObj = re.match(r'^notes-\d{2}\.\d{2}\.\d{4}$', file)
    if matchObj:
        available_backups.append(file)

last_backup = available_backups[-1]

print(available_backups)

#os.mkdir(new_dir, 0600)

# year = file[12:]
# month = file[9:11]
# http://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
if not os.path.isdir(new_dir):
    os.mkdir(new_dir, 600)
