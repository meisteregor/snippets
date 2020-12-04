import threading
import random
import time


def thread_job(results, index):
    time.sleep(1)
    results[index] = random.randint(1, 5)


def gather(threads_count):
    threads = [None] * threads_count
    results = [None] * threads_count
    for i in range(threads_count):
        threads[i] = threading.Thread(target=thread_job, args=(results, i))
        threads[i].start()
    # upper and lower same 'for' loops are necessary!
    # do some other stuff
    for i in range(threads_count):
        threads[i].join()
    return results


x = gather(random.randint(1, 9))
print(x)
