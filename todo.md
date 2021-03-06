- [ ] Change name to `visitpaths.py` or `visitfiles.py` to avoid typing underscore?

- [ ] List the matching file when skipping over an already visited directory?

- [x] Don't skip broken symlinks.

- [x] Make this work with a pipe

  - https://stackoverflow.com/questions/40270252/eoferror-when-using-input-after-using-sys-stdin-buffer-read

- [ ] Does the parent command require running with `stdbuf`?

  - https://unix.stackexchange.com/questions/25372/turn-off-buffering-in-pipe

- [x] Add an interactive option to go back to the directory just visited.

Flags to add
------------

- [ ] A `--follow-symlinks` / `-f` flag to follow symbolic links / use realpath.

- [ ] Optionally handle null-delimited paths in place of newline-delimited paths.

- [ ] Add a `--terse` or `--quiet` flag?

- [x] Add a `--parent` flag to go to the parent directory.
