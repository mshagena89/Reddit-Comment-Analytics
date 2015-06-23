import time 

date = (time.strftime("%m.%d.%Y"))
dir = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/NFL/" + date + "/"

#config vars
outFile = dir + "comments.csv"
maskpath = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Fantasy/nflMask.jpg"
parsedCommentsFile = dir + "Parsed.csv"
cloudOutput = dir + "FantasyCLoud.png"
sentimentFileOut = dir + "sentiment.csv"