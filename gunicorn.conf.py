import multiprocessing
import os

wsgi_app = "project_name.wsgi:application"
bind_port = os.getenv("PORT", "8000")
bind = f"0.0.0.0:{bind_port}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
worker_tmp_dir = "/dev/shm"
loglevel = "info"
timeout = 120