import time

def countdown(seconds):
    i = seconds
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    i = seconds
    while i > 0:
        print(f"{i} SECOND(S)!")
        time.sleep(1)
        i -= 1
    print("HAPPY NEW YEAR!")
