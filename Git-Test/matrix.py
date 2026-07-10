import random
import time
import os

os.system("")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

while True:
    print("\033[92m" + "".join(random.choice(chars) for _ in range(150)))
    time.sleep(0.02)