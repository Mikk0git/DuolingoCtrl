import time
import functions

onStartTime = time.time()
print(onStartTime)



time.sleep(0)#900)
while True:
    time.sleep(10)
    xp_today = functions.dailyXP()['xp_today']
    if time.time() - xp_today*120 > onStartTime:
        print("Zamykanie")
    print("ok")



