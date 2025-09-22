##Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def squares(num):
    time.sleep(3)
    return f"Square :{num*num}"

numbers=[1,2,3,4,5,6,7,9,10,11,12]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(squares,numbers)

    for result in results:
        print(result)
