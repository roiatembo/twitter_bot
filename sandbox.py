from datetime import datetime
import time, math
tweet_time = datetime(2023, 5, 19, 2, 12)
now = datetime.now()
current_time = now.strftime("%H:%M")
the = tweet_time.strftime("%H:%M")
wait_time = math.floor((tweet_time - now).total_seconds())

print("starting to wait")
time.sleep(wait_time)
print("finished waiting")
