I want to read a list of pathnames on stdin,
then drop into a new interactive shell in each of those directories
(or parent directory if it's a file).

This is easy enough when reading from a file,
but when reading from a pipe
the newly spawned shell consumes the rest of stdin
and then exits.

How can I stop this from happening?

Something like ``os.execlp`` is even worse,
because it replaces the parent process entirely.

Not the same as this:

https://stackoverflow.com/questions/28008594/how-do-i-fork-a-new-process-with-independent-stdout-stderr-and-stdin

because I don't want the parent process to terminate,
I want it to stick around to spawn the next shell
regardless of what happens in the child shell.

Not the same as this:

https://stackoverflow.com/questions/27624850/launch-a-completely-independent-process

https://stackoverflow.com/questions/20646519/how-to-spawn-a-new-independent-process-in-python

https://stackoverflow.com/questions/22433913/spawn-a-subprocess-in-foreground-even-after-python-exits

because I don't want the shell to stay around
after the parent process is finished.
