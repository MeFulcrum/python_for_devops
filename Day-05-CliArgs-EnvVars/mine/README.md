# Command Line Args & Environment Variables (Day-05) 📥🔧

This folder contains small example scripts demonstrating how to handle command-line
arguments and environment variables in Python 3.

Files
- `cli_args.py` — shows how to use `argparse` and also demonstrates `sys.argv` for raw access.
- `env_vars.py` — shows how to read environment variables with `os.getenv` and `os.environ`,
  and how to pass environment variables to a subprocess.

Quick examples

1) Command-line arguments (argparse):

```bash
python cli_args.py --name Alice -c 2 --verbose extra1 extra2
```

Output example:
```
[1/2] greeting='Hello, Alice!', extras=['extra1', 'extra2']
[2/2] greeting='Hello, Alice!', extras=['extra1', 'extra2']
```

2) Raw arguments via `sys.argv`:

```bash
python cli_args.py foo bar
# prints: Raw argv (excluding script name): ['foo', 'bar']
```

3) Environment variables (cross-platform):

PowerShell:
```powershell
$env:DEMO_USER='Alice'; $env:DEMO_DEBUG='1'; python env_vars.py
```

Command Prompt (cmd.exe):
```batch
set DEMO_USER=Alice && set DEMO_DEBUG=1 && python env_vars.py
```

Unix/macOS (bash/zsh):
```bash
DEMO_USER=Alice DEMO_DEBUG=1 python env_vars.py
```

Notes
- Use `os.getenv('KEY', default)` when you want a safe default.
- Use `os.environ['KEY']` only when you want a KeyError to be raised for missing keys.
- For complex CLI interfaces prefer `argparse` or third-party libs like `click`.

Enjoy! ✅
