import multiprocessing

bind = "0.0.0.0:8000"
forwarded_allow_ips = "*"
workers = multiprocessing.cpu_count() * 2 + 1
keepalive = 5
timeout = 120
