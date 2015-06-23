from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import csv 
import random

#Config Vars
outFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/comments.csv"
parsedOutFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/commentsParsed.csv"
font_path =  "C:\\Windows\\Fonts\\AGENCYR.TTF"
outCloud =  "C:/Users/Mike/Documents/GitHub/RedditAnalytics/wordCloudMask.png"


wordlist = []
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(200, 100%%, %d%%)" % random.randint(40, 80)

        
def parseComments(commentFile):
    with open(commentFile, 'rb') as readFile:
        commentReader = csv.reader(readFile)

        for row in commentReader:
            wordlist.append(row[1])
    return wordlist 

#wordList = parseComments()

def writeCommentsToCsv(commentList, outputFile):
    with open(outputFile, 'wb') as writeFile:
        writer = csv.writer(writeFile)

        for row in commentList:
            writer.writerow([row])

#writeCommentsToCsv()

#panthersmask = imread(maskpath)
#text = open(parsedOutFile).read()

#wordCloud = WordCloud(font_path = font_path, mask = panthersmask)
#wordCloud.generate(text)

#adjust colors
#default_colors = wordCloud.to_array()

#wordCloud.recolor(color_func = blue_color_func, random_state =3)

#wordCloud.to_file(outCloud)

#print "success"