import urllib.request as ur

#url = 'http://www.iheartquotes.com/api/v1/random'
url = 'https://andruxnet-random-famous-quotes.p.rapidapi.com'
conn = ur.urlopen(url)

print(conn)




