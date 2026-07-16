import random
import time
import os

def start_matrix():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

    try:
        while True:
            width = os.get_terminal_size().columns

            line = ""
            for _ in range(width):
                line += random.choice(chars)

            print("\033[92m" + line + "\033[0m")
            time.sleep(0.03)

    except KeyboardInterrupt:
        print("\n\n303 Toolkit menüsüne dönülüyor...")