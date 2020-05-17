#! /usr/bin/env python3

import argparse
import logging
import os
import subprocess
import sys

def visit_paths(read_from=sys.stdin):

    if read_from == sys.stdin:
        old_stdin = sys.stdin
        sys.stdin = open('/dev/tty')
        read_from = old_stdin

    shell_bin = os.environ['SHELL']
    logging.debug("SHELL = '{}'".format(shell_bin))
    already_visited = set()
    n_visits = 0
    n_skipped = 0
    i = None
    quit = False
    for i, line in enumerate(args.infile):
        visit_dir = None
        candidate = line.rstrip()
        logging.debug("candidate = '{}'".format(candidate))
        if os.path.isdir(candidate):
            visit_dir = candidate
        elif os.path.isfile(candidate):
            visit_dir = os.path.dirname(candidate)
        else:
            logging.warning("does not exist: '{}'".format(candidate))
            n_skipped +=1
            continue
        if visit_dir is not None:
            real_dir = os.path.realpath(visit_dir)
        else:
            # Should not happen.
            logging.warning("could not determine directory for path: '{}'".format(candidate))
            n_skipped +=1
            continue
        if visit_dir in already_visited:
            logging.info("already visited: '{}'".format(visit_dir))
            n_skipped +=1
            continue
        elif real_dir in already_visited:
            logging.info("already visited: '{}' -> '{}'".format(visit_dir, real_dir))
            n_skipped +=1
            continue

        go_back = False
        while True:
            logging.info("spawning '{}' in '{}'".format(shell_bin, visit_dir))
            run_args = [shell_bin, "-i"]
            if os.path.isfile(candidate):
                print("filename = '{}'".format(os.path.basename(candidate)))
            with open('/dev/tty') as fp_tty:
                subprocess.call(run_args, cwd=visit_dir, stdin=fp_tty)
            while True:
                try :
                    response = input("#{}. Enter 'q' to quit, 'b' to go back, or 'Enter' to continue: ".format(n_visits + 1))
                except EOFError:
                    sys.stdout.write('\n')
                    logging.debug("got Ctrl-D, quitting".format(visit_dir))
                    quit = True
                    go_back = False
                    break
                if response in ["b", "back"]:
                    logging.info("got '{}', going back to '{}'".format(response, visit_dir))
                    go_back = True
                    break
                elif response in ["q", "quit", "exit"]:
                    logging.debug("got '{}', quitting".format(response))
                    quit = True
                    go_back = False
                    break
                elif response in [""]:
                    logging.debug("got '{}', continuing".format(response))
                    go_back = False
                    break
                else:
                    logging.debug("got '{}', trying again".format(response))
                    continue
            if not go_back:
                break

        already_visited.add(visit_dir)
        already_visited.add(real_dir)
        n_visits +=1

        if quit:
            break

    if i is None:
        print("paths received: 0")
    else:
        print("paths received: {}".format(i + 1))
    print("distinct directories visited: {}".format(n_visits))
    print("duplicate paths skipped: {}".format(n_skipped))

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
    visit_paths(args.infile)
