#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # If running the development server, check for port conflicts
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        import socket
        port = sys.argv[2] if len(sys.argv) > 2 else '8000'
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', int(port)))
        except OSError:
            print(f"Port {port} is already in use. Please specify a different port using 'python manage.py runserver <port>'.")
            sys.exit(1)


if __name__ == "__main__":
    main()
