import subprocess
import os
from .builtins import BUILTINS

def execute(commands):
    if not commands:
        return

    # single command
    if len(commands) == 1:
        tokens = commands[0]
        command = tokens[0]
        args = tokens[1:]

        if command in BUILTINS:
            BUILTINS[command](args)
            return

        try:
            subprocess.run([command] + args)
        except FileNotFoundError:
            print(f"shell: command not found: {command}")

    # piped commands
    else:
        processes = []
        prev_stdout = None

        for i, tokens in enumerate(commands):
            is_last = i == len(commands) - 1
            stdin = prev_stdout

            try:
                p = subprocess.Popen(
                    tokens,
                    stdin=stdin,
                    stdout=None if is_last else subprocess.PIPE,
                    stderr=None
                )
                if prev_stdout:
                    prev_stdout.close()
                prev_stdout = p.stdout
                processes.append(p)
            except FileNotFoundError:
                print(f"shell: command not found: {tokens[0]}")
                return

        for p in processes:
            p.wait()