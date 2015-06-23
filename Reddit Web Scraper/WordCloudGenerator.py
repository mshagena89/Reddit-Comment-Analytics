from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import csv 
import random

#wordcloud generation helper functions
#see panthersScrape.py or NFLScrape.py files for usage examples

#Config Vars
outFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/comments.csv"
parsedOutFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/commentsParsed.csv"
font_path =  "C:\\Windows\\Fonts\\AGENCYR.TTF"
outCloud =  "C:/Users/Mike/Documents/GitHub/RedditAnalytics/wordCloudMask.png"

wordlist = []

#function to alter wordlcoud text to blue panthers color
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(200, 100%%, %d%%)" % random.randint(40, 80)

#parses out comment field from originally scraped .csv with all metadata       
def parseComments(commentFile):
    with open(commentFile, 'rb') as readFile:
        commentReader = csv.reader(readFile)

        for row in commentReader:
            wordlist.append(row[1])
    return wordlist 

#wordList = parseComments()

#write parsed out comments to .csv for wordcloud processing
def writeCommentsToCsv(commentList, outputFile):
    with open(outputFile, 'wb') as writeFile:
        writer = csv.writer(writeFile)

        for row in commentList:
            writer.writerow([row])
