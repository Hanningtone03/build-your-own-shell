import os
from .parser import parse
from .executor import execute

def run():
    while True:
        try:
            cwd = os.getcwd()
            line = input(f"\033[32m{cwd}\033[0m $ ")

            if not line.strip():
                continue

            commands = parse(line)
            execute(commands)

        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            break

if __name__ == "__main__":
    run()