from newspaper import Article

url = u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
a = Article(url) # Chinese

a.download()
a.parse()