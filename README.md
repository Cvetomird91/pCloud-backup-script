A simple BASH script I use to backup notes to my pCloud account, which is mounted as FUSE
after authenticating with the pCloudSync GUI desktop client.

A date is added to the name of the new backup directory. If a daily backup has already been created,
the script doesn't allow the creating of a new one, unless the --force / -f option is used.

Also, a comparison between the files in the previous backup and their current content is performed
using diff.

A file with the lines of all the files is also added to the backup.
