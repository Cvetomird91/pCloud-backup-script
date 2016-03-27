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
changes_file = new_dir + 'changes-' + current_date

for file in files:
    matchObj = re.match(r'^notes-\d{2}\.\d{2}\.\d{4}$', file)
    if matchObj:
        available_backups.append(file)

available_backups = [drive_path + available for available in available_backups]

last_backup = available_backups[-1]

arguments = argparse.ArgumentParser(description='Process options')
arguments.add_argument('--available', '-a', action='store_true')
arguments.add_argument('--force', '-f', action='store_true')
args = arguments.parse_args()
force_backup = args.force

if args.available:
    for backup in available_backups:
        print(backup)
    sys.exit(0)

def create_line_count(directory, line_count_file):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename != line_count_file and not os.path.isdir(filename):
            num_lines = sum(1 for line in open(filename))
            line_count = str(num_lines) + ' ' + filename
            file = open(line_count_file, 'a+')
            file.write(line_count + '\n')
            file.close

def diff_dir(dir_left, dir_right, output_file):

    dir_left = os.path.realpath(dir_left)
    dir_right = os.path.realpath(dir_right)

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

    files_left = os.listdir(dir_left)

    for filename in files_left:
        if not re.match(r'line_*', filename) and not re.match(r'changes-*', filename):
            file_left = dir_left + '/' + filename
            file_right = dir_right + '/' + filename
            if os.path.isfile(file_left):
                create_diff(file_left, file_right, output_file)

if force_backup or not os.path.exists(new_dir):
    os.chdir(drive_path)
    if force_backup:
        shutil.rmtree(last_backup)
        last_backup = available_backups[-2]
    shutil.copytree(notes_path, new_dir)
    diff_dir(last_backup, new_dir, changes_file)
    create_line_count(notes_path, lines_count)
else:
    print('Daily backup already created!')
