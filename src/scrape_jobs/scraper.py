import csv
from bs4 import BeautifulSoup
import requests
import re

def main() -> None:
    base_url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all job titles on the main page. Each job title is contained in an <h2> element with the class "title".
    titles = soup.find_all("h2", class_="title")
    number_job = 0

    with open("jobs.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Company", "Description", "Location"])

        for title in titles:
            # Create a URL-friendly version of the job title by replacing non-alphanumeric characters with hyphens and converting to lowercase
            title_nav = re.sub(r'[^a-zA-Z0-9]+', '-', title.get_text().lower()).rstrip('-')
            response = requests.get(f"{base_url}jobs/{title_nav}-{number_job}")
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract job details
            elements_header = soup.find("div", {'class': 'box'})
            job_title = elements_header.find("h1", class_="title")
            company = elements_header.find("h2", class_="company")
            # The description is in the first paragraph, and the location is in the second paragraph of the content div
            description = soup.select("div.content p:not(:last-child)")
            # The location is in the second paragraph, so we need to extract it and remove the "Location: " prefix
            location = re.sub(r'Location: ', '', description[1].get_text())

            # Write the job details to the CSV file
            writer.writerow([job_title.get_text(), company.get_text(), description[0].get_text(), location])
            number_job += 1
