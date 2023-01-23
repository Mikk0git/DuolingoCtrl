import duolingo
import datetime
import time

def logging():
    #LOGING -add config
    lingo  = duolingo.Duolingo('vJSVob7k', 'cinofo5012@fom8.com')



#dXP = lingo.get_daily_xp_progress()
#streak = lingo.get_streak_info()

def lang():
    logging()
    lang = lingo.get_languages(abbreviations=True)
    return lang