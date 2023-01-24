import time
import functions
import os
from datetime import date

today = date.today()
print(today)

if os.path.exists(f"onStartTime/onStartTime{today}.txt"):
    print("The file exists.")
    with open(f"onStartTime/onStartTime{today}.txt", "r") as f:
        onStartTime = f.read()
        onStartTime = float(onStartTime)
else:
    print("The file does not exist.")
    onStartTime = time.time()
    print(onStartTime)
    onStartTimeStr = str(onStartTime)
    with open(f"onStartTime/onStartTime{today}.txt", "w") as f:
        f.write(onStartTimeStr)



time.sleep(0)#900)
while True:
    time.sleep(10)
    xp_today = functions.dailyXP()['xp_today']
    if time.time() - xp_today*120 > onStartTime:
        
        print("Zamykanie")
        
    print("ok")



