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
    matchObj = re.match(r'notes-\d{2}\.\d{2}\.\d{4}$', file)
    if matchObj:
        print(file)

print(notes)
