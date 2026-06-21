#!/bin/bash

echo "Installing dependencies..."
uv sync 

echo "Collecting static files..."
uv run python manage.py collectstatic --noinput --clear