import praw
import csv
import os.path
from datetime import datetime

#Config vars
outFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/comments.csv"
csvHeader = ["Comment ID", "Comment Body", "Comment Created UTC", "Comment Created EST", "Comment Link ID", "Submission Title", "Submission ID", "Submission Date UTC", "Submission Date Local"]


########################################
#           Helper Functions           #
########################################
   
#return list of existing comment ID's in CSV to prevent dups
def CommentIdLookup(commentsFile):
    idList = []
    with open(commentsFile, 'rb') as readFile:
        commentReader = csv.reader(readFile)

        for row in commentReader:
            idList.append(row[0])
    return idList 

#returns a list of top comments for week
#loads submissions/comments from reddit.com/subreddit/top
#subreddit: str of subreddit name (i.e. "panthers")
#numposts: number of submissions to scrape 
#r: reddit praw object
def get_commentlist(subreddit, numposts, r):
    commentsList = []
    sr = r.get_subreddit(subreddit)
    print "Getting comments from posts for week...."
    count = 1

    #load all comments from each post
    for submission in sr.get_top_from_week(limit = numposts):
        submission.replace_more_comments()
        print "Loading comments for submission" + str(count)

        #get submission metadata
        submissionTitle = submission.title
        submissionId = submission.id
        submissionDateUTC = float(submission.created_utc)
        submissionDateLocal = datetime.fromtimestamp(submissionDateUTC).strftime('%Y-%m-%d %H:%M:%S')

        #append all comments/metadata to list
        for comment in praw.helpers.flatten_tree(submission.comments):
            commentDateLocal = datetime.fromtimestamp(float(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S')
            commentsList.append([unicode(comment.id).encode('utf-8'),
                                    unicode(comment.body).encode('utf-8'),
                                    comment.created_utc,
                                    commentDateLocal,
                                    unicode(comment.link_id).encode('utf-8'),
                                    unicode(submissionTitle).encode('utf-8'),
                                    unicode(submissionId).encode('utf-8'),
                                    submissionDateUTC,
                                    submissionDateLocal])
        count += 1

    print "Successfully read comments"
    return commentsList

#writes comment list output to CSV 
def commentlist_tocsv(commentList, outFile):

    with open(outFile, 'wb') as csvfile:
        commentwriter = csv.writer(csvfile)
        commentwriter.writerow(csvHeader)

        for item in commentList:
            commentwriter.writerow(item)


#takes existing scraped comments .csv file
#check for new posts on get_top_from_week
#appends post if not exists
def append_comment_list(commentsFile, numPosts, r, subreddit):

    #gets id of all existing comments in input file
    existingComments = CommentIdLookup(commentsFile)

    #get new comments
    commentList = get_commentlist(subreddit, numPosts, r)
    with open(outFile, 'ab') as csvfile:
        commentwriter = csv.writer(csvfile)

        for item in commentList:
            if item[0] not in existingComments:
                commentwriter.writerow(item)

    print "Succesfully apppended comments to" + commentsFile

#returns new comments from sub 
#equivalent scraping visiting reddit.com/r/subreddit/comments (25 results)
def GetCommentFromSubreddit(sub):
    sub_object = r.get_subreddit(sub)
    return sub_object.get_comments()
