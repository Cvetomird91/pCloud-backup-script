#!/usr/bin/env python3

import os, shutil
import datetime
import re
import difflib
import argparse
import sys, traceback

user_home = os.getenv("HOME")
drive_dir = '/pCloudDrive/'
drive_path = user_home + drive_dir
notes_path = drive_path + 'notes/'

print(notes_path)
sys.exit(0)

notes = os.listdir(notes_path)
files = os.listdir(drive_path)
available_backups = []

date = datetime.datetime.now()
current_date = date.strftime('%d.%m.%Y')
new_dir = 'notes-' + current_date
lines_count = 'lines_count-' + current_date
changes_file = 'changes-' + current_date

for file in files:
    matchObj = re.match(r'^notes-\d{2}\.\d{2}\.\d{4}$', file)
    if matchObj:
        available_backups.append(file)

last_backup = available_backups[-1]

arguments = argparse.ArgumentParser(description='Process options')
arguments.add_argument('--available', '-a', action='store_true')
arguments.add_argument('--force', '-f', action='store_true')
args = arguments.parse_args()

if args.available:
    for backup in available_backups:
        print(backup)
    sys.exit(1)

def create_line_count(directory, line_count_file):
    for filename in os.listdir(directory):
        if filename != 'lines' and not os.path.isdir(filename):
            num_lines = sum(1 for line in open(filename))
            line_count = str(num_lines) + ' ' + filename
            print(line_count)
            '''file = open('lines', 'a+')
            file.write(line_count + '\n')
            file.close'''

if args.force:
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
        shutil.copytree(notes_path, new_dir)
        create_line_count(notes_path, lines_count)
else:
    if not os.path.exists(new_dir):
        shutil.copytree(notes_path, new_dir)
        create_line_count(notes_path, lines_count)
    else:
        print('Daily backup already created!')

# year = file[12:]
# month = file[9:11]
# http://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
# http://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
# http://pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/
# https://mkaz.tech/python-argparse-cookbook.html
