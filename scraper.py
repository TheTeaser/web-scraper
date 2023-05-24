import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    """
    This function counts the number of citations needed in the provided URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations = soup.find_all("sup", class_="noprint")
    return len(citations)


def get_citations_needed_report(url):
    """
    This function provides a report of the citations needed in the given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    citations_needed = []

    for paragraph in paragraphs:
        if paragraph.find("sup", class_="noprint"):
            citation_text = paragraph.text.strip()
            citations_needed.append(citation_text)

    report = "\n\n".join(citations_needed)
    return report



URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

count = get_citations_needed_count(URL)
report = get_citations_needed_report(URL)

print("Number of citations needed:", count)
print("Citations:")
print(report)
