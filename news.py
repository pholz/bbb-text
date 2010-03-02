import feedparser
import htmlstripper

def getNews():
    #googleWorldNews = feedparser.parse("http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss")
    nytimesWorldNews = feedparser.parse("http://www.nytimes.com/services/xml/rss/nyt/World.xml")
    #print nytimesWorldNews.entries[5].keys()
    txt = []
    for i in range(len(nytimesWorldNews.entries)):
        txt.append(htmlstripper.stripHTML(nytimesWorldNews.entries[i].summary, "UTF-8"))
    
    return txt