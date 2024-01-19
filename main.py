from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.head)

title_tag = soup.title
title_content = title_tag.string
# print(title_content)  # Angela's Personal Site
print(title_tag.get_text())  # Angela's Personal Site

# print(soup.a.string)    # The App Brewery (only first anchor tag)

all_anchor_tag = soup.find_all(name="a")
print(all_anchor_tag)   # list of all anchor tags

for tag in all_anchor_tag:
    # print(tag.string)
    print(tag.get_text())   # to print content inside

    # print(tag.get("href"))
    print(tag["href"])

heading_class = soup.h3["class"]  # soup.h3.get("class")
# print(heading_class)   # ['heading']

all_heading = soup.find_all(name="h3", class_="heading")
print(all_heading)  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
print(all_heading[1].get_text())    # Other Pages

print(soup.select_one(selector="p a"))  # anchor tag inside para tag

print(soup.select("li"))
print(soup.find_all("li"))