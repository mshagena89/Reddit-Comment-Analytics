#tests 
import Reddit_Web_Scraper as scrape
import praw

#test append method on panthers file
commentsFile = "C:/Users/Mike/Documents/GitHub/RedditAnalytics/Panthers/comments.csv"
numPosts = 1
r = praw.Reddit(user_agent='comment_scraper')

scrape.append_comment_list(commentsFile, numPosts, r, "panthers")