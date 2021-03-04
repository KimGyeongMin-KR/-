import requests
from bs4 import BeautifulSoup

page_numb = 1
URL = "https://www.hankyung.com/economy?"


def get_last_page():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "paging"})

    number_page = pagination.find_all("a", {"class": None})

    numb = []
    for page in number_page:
        numb.append(int(page.string))

    last_numb = numb[-1]

    return last_numb


# URL page=page_numb


def get_article(page_last):
  hankyung_arti = []
  for page in range(page_last - 6):
    
    result = requests.get(f"{URL}page={page + page_numb}")
    soup = BeautifulSoup(result.text, "html.parser")

    article_h = soup.find_all("h3", {"class": "tit"})
    article_info = soup.find_all("div", {"class": "article_info"})
    
    for article in zip(article_h, article_info):
        article_tit = article[0].string
        article_url = article[0].find("a")["href"]
        article_day = article[1].find("span", {"class": "time"}).string
        hankyung_arti.append({
            "제목": article_tit,
            "주소": article_url,
            "날짜": article_day
        })
  return hankyung_arti


def get_article_hankyung():
  last_hankyung_page = get_last_page()

  hankyung_article = get_article(last_hankyung_page)

  return hankyung_article


