import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i} SECOND(S)!")
    print("HAPPY NEW YEAR!")
    

def countdown_with_sleep(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")
