#alarm clock with timer

from playsound import playsound

import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm (second):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < second:
        time.sleep(1)
        time_elapsed += 1

        time_left = second - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}ALARM WILL SOOUNDS IN : {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm2.wav")

minutes = int(input("how many minutes : "))
seconds = int(input("how many seconds : "))
total_second = minutes * 60 + seconds
alarm(total_second)