import WordCloudGenerator as gen
import Reddit_Web_Scraper as scraper
import datetime
import praw
from scipy.misc import imread
from wordcloud import WordCloud

print "Scraping r/Panthers comments"

#config vars
commentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/comments.csv"
parsedCommentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/Parsed.csv"
maskpath = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/Carolina-Panthers.png"
cloudOutput =  "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/Cloud.png"

#create praw object
r = praw.Reddit(user_agent='comment_scraper')

#Step 1: Scrape top comments from subreddit
results = scraper.get_commentlist("panthers", 25, r)

#Step 2: output comments to .csv
scraper.commentlist_tocsv(results, commentsFile)

#WordCloud Gen

#Step 1: Parse comments out of source CSV
parsedCommentList = gen.parseComments(commentsFile)

#Step 2: write parsed out comments to csv file 
gen.writeCommentsToCsv(parsedCommentList, parsedCommentsFile)

#Step 3: World Cloud Generation/Output
panthersmask = imread(maskpath)
text = open(parsedCommentsFile).read()

wordCloud = WordCloud(font_path = gen.font_path, mask = panthersmask)
wordCloud.generate(text)

#adjust colors
wordCloud.recolor(color_func = gen.blue_color_func, random_state =3)

wordCloud.to_file(cloudOutput)

print "success"





