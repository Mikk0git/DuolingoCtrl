import duolingo


lingo  = duolingo.Duolingo('vJSVob7k', 'cinofo5012@fom8.com')

def lang():
    
    lang = lingo.get_languages(abbreviations=True)
    return lang

def dailyXP():
    dXP = lingo.get_daily_xp_progress()
    #xp_today = dailyXP()['xp_today']
    #print(dXP)
    
    return dXP

def xpToday():
    xp_today = dailyXP()['xp_today']
    return xp_today
