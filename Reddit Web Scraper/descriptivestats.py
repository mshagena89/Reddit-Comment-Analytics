from scipy import stats
import CSVhelpers as csvhelp

path = "C:\\Users\\Mike\\Documents\\GitHub\\RedditAnalytics\\Fantasy\\06.23.2015\\sentiment.csv"

def sentiment_descriptive_stats(sentimentFile):
    results = csvhelp.csvreader_all(sentimentFile)
    return results

test = sentiment_descriptive_stats(path)

