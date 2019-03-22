test-file :
	./visit_files.py --debug example-paths.txt

test-pipe :
	printf '/etc/\n/usr/share/dict/words\n/var/' | ./visit_files.py --debug
