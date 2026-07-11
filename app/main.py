import sys

BUILTINS = {"exit", "echo", "type"}

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
                else:
                    print(f"{name}: not found")
            continue

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
