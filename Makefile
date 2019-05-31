test-file :
	./visit_paths.py --debug example-paths.txt

test-pipe :
	printf '/etc/\n/usr/share/dict/words\n/var/' | ./visit_paths.py --debug

test-pipe-fixed :
	printf '/etc/\n/usr/share/dict/words\n/var/' | ./visit_paths.py --debug /dev/fd/3 3<&0 < /dev/tty

test-slow :
	./slow-output.sh | ./visit_paths.py --debug

test-slow-pipe :
	./slow-output.sh | tee output.txt | ./visit_paths.py --debug

clean :
	rm -f -- output.txt
