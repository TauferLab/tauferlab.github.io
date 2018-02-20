import bs4
from bs4 import BeautifulSoup
import urllib.request
import re

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
            pub_type = str(element.contents)
        elif element.name == "h3":
            year = str(element.contents[0])
        elif element.name == "ol":
            for li in element.find_all("li"):
                href = li.find_all("a")
                # If there is one "<a>" tag and there are 3 elements in the li tag,
                # we have a standard citation. Everything else will be updated manually
                li = list(li)
                if(len(href)==1 and len(li) == 3):
                    # get authors
                    authors = str(li[0])

                    # get href tag
                    a_href = str(li[1])

                    # get journal/conference name
                    journal_conf = str(li[2])
                    
                    article_dict = {}
                    article_dict['pub_type'] = pub_type
                    article_dict['year'] = year
                    article_dict['authors'] = authors
                    article_dict['href'] = href
                    article_dict['journal_conf'] = journal_conf
                    dict_list.append(article_dict)
                else:
                    # Some li elements are just a newline
                    if(str(li) != "\n"):
                        manual_citations.append(str(li))

def parse_page():
    dict_list = []
    manual_citations = []
    
    page = urllib.request.urlopen("https://gcl.cis.udel.edu/publications.php")
    html_source = page.read()
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
    print(dict_list)
    print("------------------------------------")
    for citation in manual_citations:
        print(citation, "\n")
    

def main():
    parse_page()
    
if __name__== "__main__":
    main()



