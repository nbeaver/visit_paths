test-file :
	./visit_paths.py --debug example-paths.txt

test-pipe :
	printf '/etc/\n/usr/share/dict/words\n/var/' | ./visit_paths.py --debug

test-slow :
	./slow-output.sh | ./visit_paths.py --debug
