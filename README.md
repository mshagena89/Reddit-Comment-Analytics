# Reddit-Comment-Analytics

Ongoing project to scrape comments from reddit and perform text analytics.  Current focus is on 3 areas

1) Worldcloud generation

2) Sentiment Analysis

3) Tableau visualization 

Future analysis may include topic modeling/clustering. 

##Comment Scraping / Wordlcoud generation

###Comment Scraping
reddit_web_scraper.py contains helper functions to scrape top comments from subreddit

###WorldCloud Generation
Clouds are generated with https://github.com/amueller/word_cloud
For usage examples, see NFLScrape.py, PanthersScrape.py, FantasyScrape.py

###Example wordcloud output
![Alt text](https://github.com/mshagena89/Reddit-Comment-Analytics/blob/master/Reddit%20Web%20Scraper/Examples/PanthersCloud.png?raw=true "Optional title")

##Sentiment Analysis 

##Estimating Sentiment
Sentiment_calculator.py contains helper functions to calculate overall sentiment of reddit comments.
Sentiment is measured using ANEW word dictionary.

ANEW measures sentiment in 2 dimensions:

1: Valence (positive/negative)

2: Arousal (active/subdued)

By looking at combinations of these two dimensions, we are able to capture a variety of different sentiments/emotions.
For more information, see Dr. Christopher Healy's text analytics page http://www.csc.ncsu.edu/faculty/healey/maa-14/text/


###Comment Sentiment Visualization
Example sentiment dashboard can be found here: (based off a week of r/panthers comments pulled on 6.20.2015)
https://public.tableau.com/profile/michael.shagena#!/vizhome/rPanthersSentimentWeekof6_20_2015/rPanthersSentiment6_20_2015
