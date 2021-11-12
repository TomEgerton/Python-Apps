import signal
import time
import random

def receive_alarm(signum, stack):
    print ('AHHHHHHHHHHHHHHHH 👻')

ranNum = random.randint(2,9)
# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(ranNum)

print ('Start of the random whacky scream machine:', time.ctime())
time.sleep(10)
print(f'You got spooked after {ranNum} seconds')
