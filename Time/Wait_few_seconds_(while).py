import time


start_time = time.time()
print("Start time:  ", start_time)
end = start_time + 5
while True:
    if time.time() >= end:
        print("End time:    ", time.time())
        diff = time.time() - start_time
        print("Difference = ", diff)
        diff = end - start_time
        print("Difference = ", diff)
        break
