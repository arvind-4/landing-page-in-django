#!/bin/bash
uv run ruff check . --fix
uv run ruff check .
uv run ruff format .
uv run ty check .
uv run pyright .