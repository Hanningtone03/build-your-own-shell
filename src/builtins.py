import os
import sys

BUILTINS = {}

def builtin(name):
    def decorator(func):
        BUILTINS[name] = func
        return func
    return decorator

@builtin("exit")
def cmd_exit(args):
    code = int(args[0]) if args else 0
    sys.exit(code)

@builtin("echo")
def cmd_echo(args):
    print(" ".join(args))

@builtin("pwd")
def cmd_pwd(args):
    print(os.getcwd())

@builtin("cd")
def cmd_cd(args):
    path = args[0] if args else os.path.expanduser("~")
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")
    except NotADirectoryError:
        print(f"cd: {path}: Not a directory")

@builtin("clear")
def cmd_clear(args):
    os.system("cls" if os.name == "nt" else "clear")