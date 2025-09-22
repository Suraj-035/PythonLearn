'''
Real-World Example : Multiprocessing for CPU bound tasks
scenario: Factorial Calculations, especially for large numbers, involve significant computational work, 
Multiprocessing can be used to distribute the workload across multiple CPU cores, improving perfomance
'''

import multiprocessing
import math
import sys ##to increase Python's integer digit limit
import time

#increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000) ##Prevents crashes from massive factorials

##function to compute factorials of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time=time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers) #pool.map():Distributes workload across cores

    end_time=time.time()

    print(f"Results : {results}")
    print(f"Time Taken :{end_time-start_time} seconds")