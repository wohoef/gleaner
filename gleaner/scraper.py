import urllib
from collections import deque

import requests
from bs4 import BeautifulSoup


class Gleaner:
    def __init__(self, start_url, output_file):
        self.start_url = start_url
        self.base_url = urllib.parse.urlparse(start_url).netloc
        self.output_file = output_file
        self.de = deque([start_url])
        self.visited = [start_url]

    def scrape(self):
        while len(self.de) > 0:
            url = self.de.pop()
            links = self.get_a_links(url)
            links = self.filter_and_parse_links(links, url)

            self.de.extendleft(links)
            pprint(links)
            print(len(self.de))

    def get_a_links(self, url):
        links = []
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for a_tag in soup.find_all("a"):
            link = a_tag.get("href")
            links.append(link)

        return links

    def filter_and_parse_links(self, links, base):
        res = []
        for link in links:
            absolute_link = urllib.parse.urljoin(base, link)
            parsed_link = urllib.parse.urlparse(absolute_link)
            if parsed_link.netloc != self.base_url:
                continue
            normalized_link = urllib.parse.urlunparse(
                parsed_link._replace(fragment="")
            )

            res.append(
                normalized_link
            ) if normalized_link not in self.visited else ...
            self.visited.append(normalized_link)
        return res


def pprint(l):
    for ll in l:
        print(ll)
    print()
