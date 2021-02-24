from urllib.parse import urlparse
import asyncio
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urljoin
import aiohttp
from aiohttp import ClientSession
import time
from datetime import datetime
import sys, os
from bs4 import BeautifulSoup
import csv


def get_hrefs(html):
    soup = BeautifulSoup(html, "html5lib")
    a_tags = soup.find_all("a", {"href": True})
    for tag in a_tags:
        yield tag["href"]


def get_links(html, domain):

    hrefs = set()

    for href in get_hrefs(html):
        u_parse = urlparse(href)

        if u_parse.netloc == "" or u_parse.netloc == domain:
            if "#" not in href:
                hrefs.add(href)
    return hrefs


async def crawl(url, session):
    id = 0
    seedurl = url
    urlseen = set()
    urlparsed = urlparse(seedurl)
    domain = urlparsed.netloc
    url_frontier = asyncio.Queue()
    await url_frontier.put(seedurl)

    while not url_frontier.empty():
        url = await url_frontier.get()

        if url not in urlseen:
            try:
                response = await session.request(method="GET", url=url)
                response.raise_for_status()
            except:
                continue

            try:
                if response.headers["content-type"].startswith("application/"):
                    urlseen.add(url)
                    yield url
                    continue
            except KeyError:
                continue

            try:
                html = await response.text()
            except:
                continue

            urlseen.add(url)
            yield url

            for href in get_links(html, domain):
                joinlink = urljoin(seedurl, href)
                if joinlink not in urlseen:
                    await url_frontier.put(joinlink)


async def main(url):
    tasks = []
    async with ClientSession() as session:
        return await crawl(url, session)
