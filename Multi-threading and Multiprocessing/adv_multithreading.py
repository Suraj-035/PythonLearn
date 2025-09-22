## Multithreading With ThreadPool Executor: Allows you to run multiple functions in parallel threads, using a pool of worker threads.

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return(f"Numbber :{number}")

number=[1,2,3,4,5,6,7,8,9,10,11,12]

with ThreadPoolExecutor(max_workers=3) as executor: #You're creating a thread pool with 3 threads
    results=executor.map(print_number,number) #Automatically feeds elements of the list into the function in parallel.

for result in results:
    print(result)