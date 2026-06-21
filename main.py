"""Main entry point for the project."""

import sys

from gunicorn.app.wsgiapp import run


def main() -> None:
    """Run the Django app with gunicorn."""
    sys.argv = ["gunicorn", "backend.asgi:application", "-c", "gunicorn.conf.py"]
    run()


if __name__ == "__main__":
    main()
