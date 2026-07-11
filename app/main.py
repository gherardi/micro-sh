import os
import sys

BUILTINS = {"exit", "echo", "type"}

def find_executable(name):
    for directory in os.environ.get("PATH", "").split(os.pathsep):
        path = os.path.join(directory, name)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None

def main():
    while True:
        try:
            command = input("$ ")
        except EOFError:
            break

        args = command.split()
        if not args:
            continue

        if args[0] == "exit":
            code = int(args[1]) if len(args) > 1 else 0
            sys.exit(code)

        if args[0] == "echo":
            print(" ".join(args[1:]))
            continue

        if args[0] == "type":
            for name in args[1:]:
                if name in BUILTINS:
                    print(f"{name} is a shell builtin")
                    continue

                path = find_executable(name)
                if path:
                    print(f"{name} is {path}")
                else:
                    print(f"{name}: not found")
            continue

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
