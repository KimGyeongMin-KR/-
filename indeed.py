import requests
from bs4 import BeautifulSoup

page_numb = 1
URL = "https://news.joins.com/money?"


# page={page_numb}
def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    # print(a_tegs)
    # for page in pages:
    #   print(page.find("a"))
    # print(pages)
    # indeed_soup['class'] = 'paging_comm'
    # serch_soup = indeed_soup.
    pagination = soup.find("div", {"class": "paging_comm"})

    pages = pagination.find_all('a')

    a_tegs = []

    for page in pages[:-1]:
        a_tegs.append(int(page.string))

    max_page = a_tegs[-1]

    return max_page



# def test_indeed_article(last_page):

#   result = requests.get(f"{URL}page={0+ page_numb}")
#   soup = BeautifulSoup(result.text, "html.parser")

#   title = soup.find("div", {"class" : "list_basic list_sectionhome"}).find_all("h2", {"class" : "headline"}).find("a").string

#   url = soup.find("div", {"class" : "list_basic list_sectionhome"}).find_all("h2", {"class" : "headline"}).find("a")["href"]

#   day = soup.select("#content > div.list_basic.list_sectionhome > ul > li > span.byline")

#   print(day)

#   articles = []
#   for item in zip(title, url):
#     articles.append({
#       "제목"  : item[0].string.replace('\n', '').replace('\t', '').replace('  ', ''),
#       "링크"  : item[1].string.replace('\n', '').replace('\t', '').replace('  ', '')
#     })
#   print(articles)

#   #content > div.list_basic.list_sectionhome > ul > li > span.byline

#   return articles


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page-5):
    result = requests.get(f"{URL}page={page + page_numb}")
    soup = BeautifulSoup(result.text, "html.parser")

    firResults = soup.find("div", {
        "class": "list_basic list_sectionhome"
    }).find_all("h2", {"class": "headline"})
    secResults = soup.find_all("span", {"class": "byline"})

    for result in zip(firResults, secResults):

        title = result[0].find("a").string
        urlHref = result[0].find("a")["href"]
        day = result[1].string

        jobs.append({"제목": title, "주소": urlHref, "날짜": day})

  return jobs

    # for result in firResults:
    #   title = result.find_all("h2" , {"class" : "headline"}).find("a").string
    #   urlHref = result.find_all("h2" , {"class" : "headline"}).find("a")["href"]
    #   byLine = result.find_all("span" , {"class" : "byline"}).string
    #   print(title, urlHref, byLine)

    # result = requests.get(f"{URL}page={page + page_numb}")
    # print(result.status_code)

def get_article_joongang():
  last_page = extract_indeed_pages()

  article = extract_indeed_jobs(last_page)

  return article