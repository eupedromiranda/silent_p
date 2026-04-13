import time
import random
from colorama import init, Fore, Style

init()

messages = [
    "você sente algo presente",
    "está muito silencioso...",
    "algo está aqui",
    "...",
    "você ainda está aqui"
]

colors = [
    Fore.WHITE,
    Fore.CYAN,
    Fore.MAGENTA,
    Fore.GREEN
]

def ghost_event():
    print(random.choice(colors) + random.choice(messages) + Style.RESET_ALL)

def main():
    print("system running...")

    while True:
        time.sleep(random.randint(5, 18))

        if random.random() < 0.07:
            ghost_event()
        else:
            print("...")

if __name__ == "__main__":
    main()
