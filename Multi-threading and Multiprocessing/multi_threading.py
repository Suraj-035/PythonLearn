import threading
import time 
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers:  {i}")

def print_letter():
    for letter in "abcd":
        time.sleep(2)
        print(f"Letter :{letter}")

t=time.time()
print_number()
print_letter()
finished_time=time.time()-t
print(finished_time)