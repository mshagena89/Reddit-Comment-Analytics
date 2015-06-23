import anew
import WordCloudGenerator as gen
import string
import csv


commentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/comments.csv"
sentimentFileOut = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/sentimentOutput.csv"


#takes input file of comments
#outputs .csv with arousal and valance calculated foreach comment
def CalculateExportSentiment(commentsFile, sentimentOutFile):

    commentList = gen.parseComments(commentsFile)

    with open(sentimentFileOut, 'wb') as result:
        wtr = csv.writer(result)
        wtr.writerow(("Comment Body", "Arousal", "Valence"))

        for r in commentList:
            commentbody = str(r)
            stringlist = string.split(commentbody)
            sentimentResults = anew.sentiment(stringlist)

            wtr.writerow((commentbody, str(sentimentResults['arousal']), str(sentimentResults['valence'])))

    print "Outputted file to" + sentimentFileOut

#CalculateExportSentiment(commentsFile, sentimentFileOut)