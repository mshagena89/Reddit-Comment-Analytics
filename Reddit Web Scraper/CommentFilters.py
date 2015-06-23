import csv
import CSVhelpers as csvhelp

#takes list of player name terms 
#returns list of comments which contain player names
def filterCommentsByPlayer(playerNameList, commentFile):
    commentlist = csvreader(commentFile)

    for name in playerNameList:
        filteredList = [k for k in commentlist if name in k]

    return filteredList

test = filterCommentsByPlayer(["Megatron"], 'C:\\Users\\Mike\\Documents\\GitHub\\RedditAnalytics\\Fantasy\\06.23.2015\\Parsed.csv')

