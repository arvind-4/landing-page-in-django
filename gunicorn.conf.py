"""Gunicorn configuration."""

import os

bind = f"0.0.0.0:{os.getenv('APP_PORT', '8000')}"

workers = 3 if os.environ.get("APP_ENV") in ("production", "prod") else 1

# Use Uvicorn workers for ASGI applications (FastAPI, Starlette, etc.)
worker_class = "uvicorn.workers.UvicornWorker"

timeout = 120

accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOG_LEVEL", "info")

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

proc_name = "landing-page"

reload = os.environ.get("APP_ENV") not in ("production", "prod")
preload_app = os.environ.get("APP_ENV") not in ("production", "prod")
