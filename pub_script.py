import bs4
from bs4 import BeautifulSoup
import urllib.request
import re
    
def parse_publication_type(a, pub_type):
    manual_citations = []
    for element in a.contents:
        if element.name == "h3":
            year = element.contents
        elif element.name == "ol":
            for li in element.find_all("li"):
                href = li.find_all("a")
                # If there is one a tag and there are 3 elements in the li tag,
                # we have a standard citation. Everything will be updated manually
                li = list(li)
                if(len(href)==1 and len(li) == 3):
                    # get authors
                    authors = str(li[0])
                    print(authors)
                    # get href tag
                    a_href = str(li[1])
                    print(a_href)
                    # get journal/conference name
                    journal = str(li[2])
                    print(journal)
                else:
                    manual_citations.append(str(li))
        dictionary['title'] = 

def parse_page:
    page = urllib.request.urlopen("https://gcl.cis.udel.edu/publications.php")
    html_source = page.read()
    #journal_papers=
    #Book_chapters=
    #Conferences, Symposiums, Workshops
    #Poster
    #Technical Reports
    #Thesis=
    # soup = BeautifulSoup(html_source, "lxml")
    soup = BeautifulSoup(open("./publications.php"), "lxml")
    
    a = soup.find("a",{"name":"JournaplPapers"})
    parse_publication_type(a, "JournalPapers")

    a = soup.find("a",{"name":"BookChapters"})    
    parse_publication_type(a, "BookChapters")

    a = soup.find("a",{"name":"Conferences"})    
    parse_publication_type(a, "Conferences")

    a = soup.find("a",{"name":"EducationalPapers"})
    parse_publication_type(a, "EducationPapers")

    a = soup.find("a",{"name":"Posters"})
    parse_publication_type(a, "Posters")

    a = soup.find("a",{"name":"TecnicalReports"})
    parse_publication_type(a, "TechnicalReports")

    a = soup.find("a",{"name":"Thesis"})
    parse_publication_type(a, "Thesis")
    
    # a.parents gives the division containing all publications
    a = a.parent
    # Parse through every element in contents.
    # From the elements, we gather
    #     - Publication Type
    #     - Year of Publication
    #     - Full citation
    #          - Authors
    #          - Title (w/ optional url)
    #          - Journal (conference)
    #          - Additional info
    manual_citations = []

def main():
    
