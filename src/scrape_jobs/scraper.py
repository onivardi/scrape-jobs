import csv
from bs4 import BeautifulSoup
import requests
import re

def main() -> None:
    base_url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("h2", class_="title")
    number_job = 0
    jobs = []

    with open("jobs.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Company", "Description", "Location"])

        for title in titles:
            title_nav = re.sub(r'[^a-zA-Z0-9]+', '-', title.get_text().lower()).rstrip('-')
            response = requests.get(f"{base_url}jobs/{title_nav}-{number_job}")
            soup = BeautifulSoup(response.text, "html.parser")

            elements_header = soup.find("div", {'class': 'box'})
            job_title = elements_header.find("h1", class_="title")
            company = elements_header.find("h2", class_="company")
            description = soup.select("div.content p:not(:last-child)")
            location = re.sub(r'Location: ', '', description[1].get_text())

            writer.writerow([job_title.get_text(), company.get_text(), description[0].get_text(), location])
            number_job += 1
