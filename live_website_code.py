from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get(url="https://news.ycombinator.com/")
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)

article_tag = soup.find_all(name="span", attrs={"class": "titleline"})
upvote_tag = soup.find_all(name="span", attrs={"class": "subline"})

# print(article_tag)
# print(upvote_tag)

title_collection = []
vote_collection = []
author_collection = []
link_list = []
for title in article_tag:
    article_title = title.find("a").getText()
    link = title.find("a").get("href")
    title_collection.append(article_title)
    link_list.append(link)


for upvote in upvote_tag:
    upvote_number = int((upvote.find(name="span", class_="score")).getText().split()[0])
    vote_collection.append(upvote_number)
    author_name = (upvote.find(name="a", class_="hnuser")).getText()
    author_collection.append(author_name)

print(title_collection)
print(vote_collection)
print(author_collection)

hacker_news_data = {
    "title": title_collection,
    "upvote": vote_collection,
    "author_name": author_collection,
    "article_link": link_list,
}

data = pandas.DataFrame(hacker_news_data)
data.to_csv("live_web_data.csv")
# print(data)

maximum_vote = (data["upvote"]).max()
print(maximum_vote)
max_data = data[data["upvote"] == maximum_vote]
print(max_data)

max_index = vote_collection.index(maximum_vote)
print(max_data["title"][max_index], max_data["author_name"][max_index])