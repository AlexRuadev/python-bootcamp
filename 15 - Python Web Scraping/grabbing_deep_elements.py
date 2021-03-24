import requests
result = requests.get("https://www.pimclick.com/")


import bs4

soup = bs4.BeautifulSoup(result.text, "lxml")

# Getting the h3 string in dextra div in works id
x = soup.select('#works .dextra h3')[0].getText()
print(x)