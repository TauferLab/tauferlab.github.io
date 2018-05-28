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



def parse_page():
    news_items = []
    
    html_source = open("news.php", 'r')
    soup = BeautifulSoup(html_source, "lxml")
    
    div = soup.find("div",{"id":"content"})
    news_items = parse_news_items(div, news_items)

    # dict_list = sort_years_and_pub_type(dict_list)
    # print(dict_list)
    # new_webpage = render("./publications.html", dict_list)
    # with open("./new_publications.html", 'w') as f:
    #     f.write(new_webpage)

def parse_news_items(div, news_items):
    # div is all the html within the div tags. It containts all the news entries
    for element in div.contents:
        # p containts the news title and date (the <b> tag) and the description (<br> tag)
        if element.name == "p":
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
            entry_dict ={}
            # print(child)
            # print(date_groups.group(2))
            entry_dict['month'] = date_groups.group(1)
            if date_groups.group(2) != None:
                entry_dict['date'] = date_groups.group(2)
            entry_dict['year'] = date_groups.group(3)
            entry_dict['title'] = date_groups.group(4)
            entry_dict['content'] = str(news_info)
        elif element.name == "table":
            print('test')
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
