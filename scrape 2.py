
import time
import urllib.request

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Wheeler_Dealers_episodes'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
rows = soup.find_all('tr')
print(rows[:10])
