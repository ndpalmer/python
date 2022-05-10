import requests
from bs4 import BeautifulSoup
import pprint

def get_pages(n):
  for pages in range(0,n):
    res = requests.get(f'https://news.ycombinator.com/news?p={n}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    return create_custom_hn(links, subtext)

def sort_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'])

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_by_votes(hn)

pprint.pprint(get_pages(2))