import feedparser
import htmlstripper
import re

#feed = feedparser.parse("http://rss.news.yahoo.com/rss/world")
feed = feedparser.parse("http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss")
#print nytimesWorldNews.entries[5].keys()
txt = []
for i in range(len(feed.entries)):
   # if "content" in feed.entries[i].keys():
        print re.search("src=\"(.[^\"]*)\"",feed.entries[i].summary).group(1)