#! /usr/bin/env python

import argparse
import logging
import os
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Visit files from file or stdin.'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        help='More verbose logging',
        dest="loglevel",
        default=logging.WARNING,
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        '-d',
        '--debug',
        help='Enable debugging logs',
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
    )
    parser.add_argument(
        'infile',
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Input file (or stdin)',
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    directories_to_visit = set()
    for line in args.infile.readlines():
        visit_dir = None
        candidate = line.rstrip()
        logging.debug("candidate = '{}'".format(candidate))
        if os.path.isdir(candidate):
            visit_dir = candidate
        elif os.path.isfile(candidate):
            visit_dir = os.path.dirname(candidate)
        else:
            logging.warning("does not exist: '{}'\n".format(candidate))
            continue
        if visit_dir is not None:
            real_dir = os.path.realpath(visit_dir)
            directories_to_visit.add(real_dir)
        else:
            # Should not happen.
            logging.warning("could not determine directory for path: '{}'\n".format(candidate))
            continue

    shell_bin = os.environ['SHELL']
    logging.debug("SHELL = '{}'".format(shell_bin))
    for directory in directories_to_visit:
        logging.info("spawning '{}' in '{}'".format(shell_bin, directory))
        run_args = [shell_bin, "-i"]
        subprocess.Popen(["/bin/bash", "-i"], shell=True, cwd=directory, stdin=sys.stdin)
