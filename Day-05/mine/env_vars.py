"""Environment variable examples for Day-05

Shows reading environment variables (cross-platform examples included).

Usage examples (Windows PowerShell):
  $env:DEMO_USER='Alice'; $env:DEMO_DEBUG='1'; python env_vars.py

Windows Command Prompt (cmd.exe):
  set DEMO_USER=Alice && set DEMO_DEBUG=1 && python env_vars.py

Unix/macOS:
  DEMO_USER=Alice DEMO_DEBUG=1 python env_vars.py
"""

from __future__ import annotations
import os
import subprocess


def show_env_vars() -> None:
    # Prefer os.getenv when a default is useful
    user = os.getenv('DEMO_USER', 'guest')
    debug_flag = os.getenv('DEMO_DEBUG', '0')
    debug = debug_flag in ('1', 'true', 'True')

    # os.environ[...] raises KeyError if missing; use .get() to avoid exceptions
    secret = os.environ.get('DEMO_SECRET')

    print(f"DEMO_USER = {user}")
    print(f"DEMO_DEBUG = {debug} (raw='{debug_flag}')")
    print(f"DEMO_SECRET = {'<set>' if secret else '<not set>'}")


def show_subprocess_example() -> None:
    # Demonstrate passing env vars to a child process without modifying the parent's environment
    child_env = {**os.environ, 'CHILD_VAR': 'child_value_example'}
    print("\nLaunching short subprocess that prints CHILD_VAR:")
    result = subprocess.run([
        'python', '-c', "import os; print('CHILD_VAR=' + os.getenv('CHILD_VAR','<not set>'))"
    ], env=child_env, capture_output=True, text=True)
    print(result.stdout.strip())


def main() -> None:
    show_env_vars()
    show_subprocess_example()


if __name__ == '__main__':
    main()
