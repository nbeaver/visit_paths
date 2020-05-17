- [ ] Make this work with a pipe, maybe like this?

    if read_from == sys.stdin:
        old_stdin = sys.stdin
        sys.stdin = open('/dev/tty')
        read_from = old_stdin

https://stackoverflow.com/questions/40270252/eoferror-when-using-input-after-using-sys-stdin-buffer-read

- [ ] Does the parent command require running with `stdbuf`?

  - https://unix.stackexchange.com/questions/25372/turn-off-buffering-in-pipe

- [ ] Add a `--terse` or `--quiet` flag?

- [x] Add an interactive option to go back to the directory just visited.
