all :
	printf '/etc/\n/usr/share/dict/words\n/var/' | ./visit_files.py --debug
