#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line, get_commands
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    commands = list(get_commands().keys()) + ['help', '--help']
    if sys.argv[1] in commands:
        execute_from_command_line(sys.argv)
    else:
        import subprocess
        subprocess.run(sys.argv[1:])
