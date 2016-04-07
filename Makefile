install:
	if ! test -d /home/$(USER)/bin; then mkdir /home/$(USER)/bin/; fi
	cp backup-notes /home/$(USER)/bin/
