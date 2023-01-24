import duolingo
import time

def lang():
    lingo  = duolingo.Duolingo('vJSVob7k', 'cinofo5012@fom8.com')
    lang = lingo.get_languages(abbreviations=True)
    return lang

def dailyXP():
    lingo  = duolingo.Duolingo('vJSVob7k', 'cinofo5012@fom8.com')
    dXP = lingo.get_daily_xp_progress()
    print(dXP)
    xp_today = dXP['xp_today']
    return xp_today

onStartTime = time.time()

print(onStartTime)

time.sleep(5)#900)
while True:
    if time.time() - dailyXP()*120 > onStartTime:
        print("Zamykanie")
    



