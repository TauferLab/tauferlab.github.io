import bs4
from bs4 import BeautifulSoup
import urllib.request
import re
import jinja2
import argparse
import os

# John Bounds
# GCLab
# Feb 8 2018
# ---------------------------------------
# Script objective:
# Parse through every element in contents.
# From the elements, we gather
#     - Publication Type
#     - Year of Publication
#     - Full citation
#          - Authors
#          - Title (w/ optional url)
#          - Journal (conference)
#          - Additional info

def parse_publication_type(a, dict_list, manual_citations):
    for element in a.contents:
        if element.name == "a":
            print(str(element.contents))
            pub_type = str(element.contents).replace('[<h2>','').replace('</h2>]','')
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
                        
def render(tpl_path, dict_list):
            path, filename = os.path.split(tpl_path)
            return jinja2.Environment(
                loader=jinja2.FileSystemLoader(path or './')
            ).get_template(filename).render(dict_list=dict_list)

def parse_page():
    dict_list = []
    manual_citations = []
    
    # page = urllib.request.urlopen("https://gcl.cis.udel.edu/publications.php")
    # html_source = page.read()
    html_source = open("./gcl_publications.php", 'r')
    #journal_papers=
    #Book_chapters=
    #Conferences, Symposiums, Workshops
    #Poster
    #Technical Reports
    #Thesis=
    soup = BeautifulSoup(html_source, "lxml")
    # soup = BeautifulSoup(open("./publications.php"), "lxml")
    
    a = soup.find("a",{"name":"JournalPapers"}).parent
    parse_publication_type(a, dict_list, manual_citations)
    # print(dict_list)
    # print("------------------------------------")
    # for citation in manual_citations:
    #     print(citation, "\n")

    dict_list = sort_years_and_pub_type(dict_list)
    print(dict_list)
    new_webpage = render("./publications.jinja2", dict_list)
    with open("./new_publications.html", 'w') as f:
        f.write(new_webpage)

    

def sort_years_and_pub_type(dict_list):
    year='0'
    #Item is a citation from publications
    for item in dict_list:
        if item['year'] != year:
            year = item['year']
            item['new_year'] = year
        else:
            item['new_year'] = 'skip'
            
    pub_type=['0']
    for item in dict_list:
        if item['pub_type'] != pub_type:
            pub_type = item['pub_type']
            item['new_pub'] = pub_type
            year = item['year']
            item['new_year'] = year
        else:
            item['new_pub'] = 'skip'

    # for item in dict_list:
    #     print(item['new_year'])
    #     print(item['new_pub'])
        
    return(dict_list)
    
def main():
    parse_page()
    
if __name__== "__main__":
    main()



