import time
from util.progress import default_progress_bar

for i in default_progress_bar(range(100)):
    time.sleep(0.02)