import duolingo

lingo  = duolingo.Duolingo('vJSVob7k', 'cinofo5012@fom8.com')

print(lingo.get_languages(abbreviations=True))
print(lingo.get_daily_xp_progress())
print(lingo.get_streak_info())