from bs4 import BeautifulSoup
import requests
import re

def main() -> None:
    
    base_url = "https://realpython.github.io/fake-jobs/"

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all h2, and substite all symbols and spaces with '-'
    titles = soup.find_all("h2", class_="title")
    number_job = 0
    for title in titles:
        title_nav = re.sub(r'[^a-zA-Z0-9]+', '-', title.get_text().lower()).rstrip('-')

        response = requests.get(f"{base_url}jobs/{title_nav}-{number_job}")
        soup = BeautifulSoup(response.text, "html.parser")

        print(f"{base_url}jobs/{title_nav}-{number_job}")
        print(soup.find("div", {'class': 'box'}))
        number_job += 1
