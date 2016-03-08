#!/usr/bin/env python3

import os
import datetime
import pathlib
import re

user_home = os.getenv("HOME")
drive_dir = '/pCloudDrive/'
drive_path = user_home + drive_dir

files = os.listdir(drive_path)
available_backups = []

for f in files:
    matchObj = re.match(r'notes-\d{2}\.\d{2}\.\d{4}$', f)
    if matchObj:
        print(f)
