import sys  
sys.path.insert(0, 'C:/Users/Mike/documents/visual studio 2013/Projects/Reddit Web Scraper/Reddit Web Scraper/')

import WordCloudGenerator as gen
import Reddit_Web_Scraper as scraper
import SentimentCalculator as sentiment
import datetime
import praw
from scipy.misc import imread
from wordcloud import WordCloud
import os
import time

import nflscrapeconfigs as config

print "Scraping r/nfl comments"

#import config variables
date = config.date
dir = config.dir
outFile = config.outFile
maskpath = config.maskpath
parsedCommentsFile = config.parsedCommentsFile
cloudOutput = config.cloudOutput
sentimentFileOut = config.sentimentFileOut


#create new folder if doesn't exist
if not os.path.exists(dir):
    os.makedirs(dir)


#create praw object
r = praw.Reddit(user_agent='comment_scraper')

#Step 1: Scrape top comments from subreddit
results = scraper.get_commentlist("nfl", 20, r)

##Step 2: output comments to .csv
scraper.commentlist_tocsv(results, outFile)

#parse out comments
parsedCommentList = gen.parseComments(outFile)
                                      
#Step 2: write parsed out comments to csv file 
gen.writeCommentsToCsv(parsedCommentList, parsedCommentsFile)


##Step 3: World Cloud Generation/Output
nflMask = imread(maskpath)
text = open(parsedCommentsFile).read()

#just use the NFL mask for now
wordCloud = WordCloud(font_path = gen.font_path, mask = nflMask)
wordCloud.generate(text)

wordCloud.to_file(cloudOutput)

##End WorldCloud Gen

#Start Sentiment Analysis
sentiment.CalculateExportSentiment(outFile, sentimentFileOut)


print "success"


