# Scrapping two pages from Hacker News sites, getting article title, link and points of articles having more than 100 points in decreasing order of votes
# Invokation: python3 scrap.py

import requests
from bs4 import BeautifulSoup
import pprint                         # Pretty print

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')        # ClassName
subtext = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links+links2
mega_subtext = subtext+subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for ind, item in enumerate(links):
        title = links[ind].getText()
        href = links[ind].get('href', None)
        vote = subtext[ind].select('.score')
        if(len(vote) != 0):                  # Some links don't have votes
            points = int(vote[0].getText().replace(' points', ''))
            if(points > 100):
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
