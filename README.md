
# scrape-jobs

A small Python utility to scrape job listings and save them to a CSV file.

## Summary

`scrape-jobs` contains a simple scraper that collects job postings and writes them to `jobs.csv` in the repository root. It's intended as a lightweight example and starting point for more advanced scraping workflows.

## Features

- Scrape job listing data from configured sources
- Save results to `jobs.csv`
- Minimal, easy-to-read code in `src/scrape_jobs/scraper.py`

## Requirements

- Python 3.10 or newer
- Optional: a virtual environment for isolation

## Quickstart 

```powershell
uv run scrape_jobs
```


Running the script produces `jobs.csv` in the repository root.

## Usage

- Edit `src/scrape_jobs/scraper.py` to adjust targets, parsing rules, or output formatting.
- Re-run the script to refresh `jobs.csv`.

## Project structure

- `src/scrape_jobs/` — package source code
- `src/scrape_jobs/scraper.py` — main scraper implementation
- `jobs.csv` — sample or generated output
- `pyproject.toml` — project metadata and dependencies

## Contributing

Contributions are welcome. Open an issue or submit a pull request with a clear description of the change.

## Notes

- This project is a starting point. If you plan to scrape third-party websites, ensure you follow their `robots.txt` rules and terms of service.
- Add a `requirements.txt` or pin dependencies in `pyproject.toml` before deploying or sharing.
- ROADMAP [https://roadmap.sh/projects/job-listings-scraper]

