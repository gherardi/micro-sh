# Shell (Python)

A POSIX-ish shell built for the [CodeCrafters "Build your own Shell"](https://codecrafters.io/challenges/shell) challenge.

It reads a line, splits it into a command and arguments, and dispatches to a builtin. If the command isn't a builtin, the shell searches `PATH` for a matching executable and runs it with the given arguments. If nothing matches, it prints a `command not found` message.

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

## External programs

Any command that isn't a builtin is resolved with the same `PATH` search `type` uses, then run in a child process with the command-line arguments passed through. The program receives the name as typed as its `argv[0]`, not the resolved path.

Example session:

```
$ echo hello world
hello world
$ type echo
echo is a shell builtin
$ type ls
ls is /bin/ls
$ ls /nonexistent
ls: /nonexistent: No such file or directory
$ type nonexistent
nonexistent: not found
$ nonexistent
nonexistent: command not found
$ exit 0
```

## Layout

- `app/main.py` — the REPL, builtin dispatch, and `find_executable()` for the `PATH` search, shared by `type` and external-program execution. `BUILTINS` is the single source of truth for builtin names.
- `your_program.sh` — local runner; mirrors `.codecrafters/run.sh`, which is what CodeCrafters runs remotely.
- `codecrafters.yml` — buildpack / debug settings for the remote runner.

## Notes

- `PATH` is split on `os.pathsep`, so the delimiter is correct on any platform.
- The REPL exits cleanly on EOF (Ctrl-D).
- Empty input lines are ignored.
