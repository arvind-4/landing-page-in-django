#!/bin/bash
uv run --env-file=.env.local python manage.py collectstatic --noinput --clear --ignore admin