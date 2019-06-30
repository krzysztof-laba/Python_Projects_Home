import time

print("\nCurrent date from PC:")
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(date)
