from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("https://gcl.cis.udel.edu/publications.php") as page:
    html_source = page.read()

    soup = BeautifulSoup(html_source, "lxml")
    print(soup.find_all("h2"))
