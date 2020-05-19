==============
visit_paths.py
==============

Description
-----------

Visit paths from a file or stdin.

Specifically, the script reads a list of pathnames
on stdin or from the given file,
then drops into a new interactive shell in each of those directories
(or parent directory if it's a file).

Features:

- Slow-running processes continue to run in the background
  while interactive shell is running.

- Prompt allow re-visiting last directory.

- Prompt allows early exit.

Example usage
-------------

Find world-readable files in `$HOME`::

    find $HOME '!' -type l -perm 777 | ./visit_paths.py

Find broken symbolic links in `$HOME`::

    find $HOME -xtype l | ./visit_paths.py

Visit git repositories under current directory::

    find . -type d -name '.git' | ./visit_paths.py --parent
