import WordCloudGenerator as gen
import Reddit_Web_Scraper as scraper
import datetime
import praw
from scipy.misc import imread
from wordcloud import WordCloud

#Scrape comments from r/nfl and generate word cloud

print "Scraping r/NFL comments"
#config vars
outFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/NFL/comments.csv"
maskpath = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/NFL/nflMask.jpg"
parsedCommentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/NFL/Parsed.csv"
cloudOutput = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/NFL/NFLCloud.png"


#create praw object
#r = praw.Reddit(user_agent='comment_scraper')

#Step 1: Scrape top comments from subreddit
#results = scraper.get_commentlist("nfl", 20, r)

#Step 2: output comments to .csv
#scraper.commentlist_tocsv(results, outFile)

#parse out comments
#parsedCommentList = gen.parseComments(outFile)
                                      
#Step 2: write parsed out comments to csv file 
#gen.writeCommentsToCsv(parsedCommentList, parsedCommentsFile)


#Step 3: World Cloud Generation/Output
nflMask = imread(maskpath)
text = open(parsedCommentsFile).read()

wordCloud = WordCloud(font_path = gen.font_path, mask = nflMask)
wordCloud.generate(text)

#adjust colors
#wordCloud.recolor(color_func = gen.blue_color_func, random_state =3)

wordCloud.to_file(cloudOutput)

print "success"








