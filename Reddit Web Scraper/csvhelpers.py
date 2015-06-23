import csv 

#CSV Read and write Helper functions

#returns list of comments from csv source file
#sourceFile: .csv with one column of comment
def csvreader(sourceFile):
    commentList = []
    with open(sourceFile, 'rb') as readFile:
        commentReader = csv.reader(readFile)

        for row in commentReader:
            commentList.append(row[0])
    return commentList 