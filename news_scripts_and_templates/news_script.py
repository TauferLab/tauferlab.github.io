import bs4
from bs4 import BeautifulSoup
import urllib.request
import re
import jinja2
import argparse
import os

# John Bounds
# GCLab
# May 2 2018
# ---------------------------------------
# Script objective:

def render(tpl_path, news_items):
            path, filename = os.path.split(tpl_path)
            return jinja2.Environment(
                loader=jinja2.FileSystemLoader(path or './')
            ).get_template(filename).render(news_items=news_items)


def parse_page():
    news_items = []
    
    html_source = open("news.php", 'r')
    soup = BeautifulSoup(html_source, "lxml")
    
    div = soup.find("div",{"id":"content"})
    news_items = parse_news_items(div, news_items)

    new_webpage = render("./news_template.html", news_items)
    with open("../new_news.html", 'w') as f:
        f.write(new_webpage)

def parse_news_items(div, news_items):
    # div is all the html within the div tags. It containts all the news entries
    for element in div.contents:
        # p containts the news title and date (the <b> tag) and the description (<br> tag)
        entry_dict = {}        
        if element.name == "p":
            first_image = 0
            if element.decode_contents() == "\n":
                continue
            # The two
            element = element.decode_contents().replace("\n", " ")
            # print(element)
            content = re.search("<b>(.*)</b>(?:<br/?>)?(.*)", element)
            # print(content)
            # file = open("test", 'w')
            # file.write(element)
            news_date_and_title = content.group(1)
            news_info = content.group(2)
            date_groups = re.search(' ?(\w*) (.*,)? *(\d*). (.*)', news_date_and_title)
            entry_dict['month'] = date_groups.group(1)
            if date_groups.group(2) != None:
                entry_dict['date'] = date_groups.group(2).replace(',','')
            else:
                entry_dict['date'] = 'skip'
                
            entry_dict['year'] = date_groups.group(3)
            entry_dict['title'] = date_groups.group(4)
            entry_dict['content'] = str(news_info)
        elif element.name == "table":
            first_image += 1
            if first_image == 1:
                image = str(element.img).replace('src="images/','src="assets/gcl-images/')
                news_items[-1]['image'] = image
        if entry_dict != {}:
            news_items.append(entry_dict)
            
        # else:
        # # Some li elements are just a newline
        #     if(str(li) != "\n"):
        #         manual_citations.append(str(li))
    return news_items

        
def main():
    parse_page()
    
if __name__== "__main__":
    main()
