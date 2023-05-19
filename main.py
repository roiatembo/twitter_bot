from datetime import datetime
import random, time, math
# This bot needs to be able to tweet between 5 - 20 times in a day

tweet_times = random.randint(5, 20)

tweet_hours = []
tweet_minutes = []

while tweet_times > 0:
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    tweet_hours.append(hour)
    tweet_minutes.append(minute)
    tweet_times -= 1

def instertion_sort(tweet_hours):
    for i in range(1, len(tweet_hours)):
        j = i - 1
        temp_hour = tweet_hours[i]
        while j>= 0 and tweet_hours[j] > temp_hour:
            tweet_hours[j + 1] = tweet_hours[j]
            j -= 1
        tweet_hours[j+1] = temp_hour
    
    return tweet_hours
print(tweet_hours)
instertion_sort(tweet_hours)
print(tweet_hours)
print(tweet_minutes)
full_tweet_times = []
for index in range(0, len(tweet_hours)):
    full_tweet_times.append({"hour": tweet_hours[index], "minute":tweet_minutes[index]})

print(full_tweet_times)

# on first run of the day, it gets the date and time
current_time = datetime.now()
# get the year month and day of today 
year = int(current_time.strftime("%Y"))
month = int(current_time.strftime("%m"))
day = int(current_time.strftime("%d"))

for schedule in full_tweet_times:
    tweet_time = datetime(year, month, day, schedule["hour"], schedule["minute"])
    now = datetime.now()
    wait_time = math.floor((tweet_time - now).total_seconds())
    time.sleep(wait_time)
    print("I tweeted")
