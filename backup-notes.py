#!/usr/bin/env python3

import os
import shutil
import datetime
import re
import difflib
import argparse
import sys

user_home = os.getenv("HOME")
drive_dir = '/pCloudDrive/'
drive_path = user_home + drive_dir
notes_path = drive_path + 'notes/'

notes = os.listdir(notes_path)
files = os.listdir(drive_path)
available_backups = []

date = datetime.datetime.now()
current_date = date.strftime('%d.%m.%Y')
new_dir = drive_path + 'notes-' + current_date + '/'
lines_count = new_dir + 'lines_count-' + current_date
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
force_backup = args.force

if args.available:
    for backup in available_backups:
        print(backup)
    sys.exit(1)

def create_line_count(directory, line_count_file):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename != line_count_file and not os.path.isdir(filename):
            num_lines = sum(1 for line in open(filename))
            line_count = str(num_lines) + ' ' + filename
            file = open(line_count_file, 'a+')
            file.write(line_count + '\n')
            file.close

'''loop over notes filenames and append path name'''
def create_diff(file_1, file_2, output_file):
    with open (file_1, 'r') as left_file:
        data_left = left_file.readlines()
        data_left = [x.strip('\n') for x in data_left]

    with open(file_2, 'r') as right_file:
        data_right = right_file.readlines()
        data_right = [x.strip('\n') for x in data_right]

    file_handle = open(output_file, 'a+')

    for line in difflib.unified_diff(data_left, data_right):
        file_handle.write(line + '\n')

    file_handle.close

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

def perform_backup():
        if force_backup or not os.path.exists(new_dir):
            if force_backup:
                shutil.rmtree(notes_path)
            shutil.copytree(notes_path, new_dir)
            create_line_count(notes_path, lines_count)
        else:
            print('Daily backup already created!')
