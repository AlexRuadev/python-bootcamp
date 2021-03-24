# pip install requests
# pip install lxml
# pip install bs4

import requests

result = requests.get("https://www.pimclick.com/")

# print(type(result))

import bs4

soup = bs4.BeautifulSoup(result.text, "lxml")
# grabbing the h1 from our page
print(soup.h1)

# grabbing all h2
# print(soup.select('h2'))

# grabbing the first h2 element
# print(soup.select('h2')[0])

# grabbbing the first h2 string
x = soup.select('h2')[0].getText()
print(x)


site_p = soup.select('p')[3].getText()
print(site_p)