import requests
url = 'https://www.pimclick.com/'
result = requests.get(url)


import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")

x = soup.select('img.above-smartphone')
# print(x)

# Check more on internet about web scrapping images
