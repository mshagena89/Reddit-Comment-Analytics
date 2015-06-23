#tests 
import Reddit_Web_Scraper as scrape
import praw
import CommentFilters as cf

#test append method on panthers file
def append_comment_list_test():
    commentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/comments.csv"
    numPosts = 1
    r = praw.Reddit(user_agent='comment_scraper')
    scrape.append_comment_list(commentsFile, numPosts, r, "panthers")


#test comment filter 
def filterCommentsByPlayer_test():
    test = cf.filterCommentsByPlayer(["Megatron"], 'C:\\Users\\Mike\\Documents\\GitHub\\RedditAnalytics\\Fantasy\\06.23.2015\\Parsed.csv')
    return test

results = filterCommentsByPlayer_test()