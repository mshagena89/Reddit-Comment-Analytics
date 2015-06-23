import praw
import csv
import os.path


#returns new comments from sub 
#equivalent scraping visiting reddit.com/r/subreddit/comments (25 results)
def GetCommentFromSubreddit(sub):
    sub_object = r.get_subreddit(sub)
    return sub_object.get_comments()


##checks for new comments on subreddit, and appends id, date, and text to output file
#def WriteCommentsToCSV(comments, out):
#    existingComments = CommentIdLookup()
#    path = out + "comments.csv"

#    with open(path, 'wb') as csvfile:
#        commentwriter = csv.writer(csvfile)
#        commentwriter.writerow(["Comment_ID", "Comment_Body", "Created_UTC", "Link_ID", "Link_Title"])
#        for comment in results: 

#            if comment.id not in existingComments:
#                row = [unicode(comment.id).encode('utf-8'),
#                         unicode(comment.body.encode('utf-8')), 
#                         comment.created_utc, 
#                         unicode(comment.link_id).encode('utf-8'), 
#                         unicode(comment.link_title).encode('utf-8')]
#                commentwriter.writerow(row)

