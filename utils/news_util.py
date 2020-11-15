from utils.speak_util import SpeakText
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def speak_news():
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    x = 0
    for news in news_list:
        if (x < 12):
            SpeakText(news.title.text)
            SpeakText(" " * 20)
            x = x + 1