from time import sleep
from rich.progress import track

for steg in track(range(10)):
    sleep(1)
