# Shell (Python)

A POSIX-ish shell built for the [CodeCrafters "Build your own Shell"](https://codecrafters.io/challenges/shell) challenge.

It reads a line, splits it into a command and arguments, and dispatches to a builtin. Anything unrecognized prints a `command not found` message. Running external programs comes in a later stage — for now only `type` resolves them, via a `PATH` search.

## Running

```sh
./your_program.sh
```

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14 (pinned in `.python-version` / `codecrafters.yml`).

## Builtins

| Command | Behavior |
| --- | --- |
| `exit [n]` | Terminates the shell with status `n` (default `0`). |
| `echo [args...]` | Prints the arguments separated by spaces, followed by a newline. |
| `type <name>...` | Reports how each name would be interpreted — see below. |

`type` resolves a name in this order:

1. If it is a builtin, print `<name> is a shell builtin`.
2. Otherwise search each directory in `PATH`, in order, for a file with that name that has the execute bit set. The first match prints `<name> is <full_path>`. Files that exist but are not executable are skipped, as are `PATH` entries that don't exist on disk.
3. If nothing matches, print `<name>: not found`.

Example session:

```
$ echo hello world
hello world
$ type echo
echo is a shell builtin
$ type ls
ls is /bin/ls
$ type nonexistent
nonexistent: not found
$ nonexistent
nonexistent: command not found
$ exit 0
```

## Layout

- `app/main.py` — the REPL, builtin dispatch, and `find_executable()` for the `PATH` search. `BUILTINS` is the single source of truth for builtin names.
- `your_program.sh` — local runner; mirrors `.codecrafters/run.sh`, which is what CodeCrafters runs remotely.
- `codecrafters.yml` — buildpack / debug settings for the remote runner.

## Notes

- `PATH` is split on `os.pathsep`, so the delimiter is correct on any platform.
- The REPL exits cleanly on EOF (Ctrl-D).
- Empty input lines are ignored.
