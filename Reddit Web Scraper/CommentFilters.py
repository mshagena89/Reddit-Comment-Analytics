import csv
import CSVhelpers as csvhelp

#takes list of player name terms 
#returns list of comments which contain player names

##TODO: build logic to filter out comments only for individual player
##find matches of player name, exclude list of non-players?
def filterCommentsByPlayer(playerNameList, commentFile):
    commentlist = csvhelp.csvreader(commentFile)

    for name in playerNameList:
        filteredList = [k for k in commentlist if name in k]

    return filteredList



