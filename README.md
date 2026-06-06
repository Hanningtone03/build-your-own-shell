# Build Your Own Shell

A Unix shell built from scratch in Python — supports pipes, built-in commands, and external program execution.

## How it works

A shell is just a loop that reads input, parses it, and executes it. This project implements that from scratch:

- Reads user input and displays a prompt with the current directory
- Parses commands including quoted strings and pipe operators
- Executes built-in commands directly within the shell process
- Runs external programs as subprocesses
- Chains commands together using pipes

## Project structure
## Running locally

```bash
python -m src.shell
```

## Supported commands

| Command | Example | Description |
|---------|---------|-------------|
| echo | `echo hello world` | Print text |
| pwd | `pwd` | Print current directory |
| cd | `cd foldername` | Change directory |
| clear | `clear` | Clear the screen |
| exit | `exit` | Exit the shell |
| pipes | `echo hello \| cat` | Chain commands together |
| any program | `python script.py` | Run any installed program |

## Tech

- Python 3
- `os` and `subprocess` modules
- No external dependencies