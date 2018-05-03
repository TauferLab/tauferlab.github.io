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
    parse_publication_type(div, news_items)

    # dict_list = sort_years_and_pub_type(dict_list)
    # print(dict_list)
    # new_webpage = render("./publications.html", dict_list)
    # with open("./new_publications.html", 'w') as f:
    #     f.write(new_webpage)

def parse_news_items(div, news_items):
    for element in div.contents:
        if element.name == "p":
            element = element.child
            print(str(element.contents))
             = str(element.contents).replace('[<h2>','').replace('</h2>]','')
        elif element.name == "h3":
            year = str(element.contents[0])
        elif element.name == "ol":
            for li in element.find_all("li"):
                href = li.find_all("a")
                # If there is one "<a>" tag and there are 3 elements in the li tag,
                # we have a standard citation. Other entries will be updated manually
                li = list(li)
                if(len(href)==1 and len(li) == 3):
                    # get authors
                    authors = str(li[0])

                    # get href tag
                    a_href = str(li[1])

                    # get journal/conference name
                    journal_conf = str(li[2]).lstrip(". ")
                    
                    article_dict = {}
                    article_dict['pub_type'] = pub_type
                    article_dict['year'] = year
                    article_dict['authors'] = authors
                    article_dict['href'] = a_href.lstrip("[").rstrip("[")
                    article_dict['journal_conf'] = journal_conf
                    dict_list.append(article_dict)
                else:
                    # Some li elements are just a newline
                    if(str(li) != "\n"):
                        manual_citations.append(str(li))


        
def main():
    parse_page()
    
if __name__== "__main__":
    main()
