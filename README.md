# Web-Scrapper-and-Data-Analysis
Web Scraper & Data Analysis Project

This project demonstrates scraping quotes data from quotes.toscrape.com, performing basic data cleaning and exploratory analysis, and storing the processed data in a SQLite database using Python. It supports data visualization and SQL-based querying for insight.

Project Structure

web_scraper_project/

├── db/                     # Folder containing SQLite database (quotes.db)
├── scraper.py              # Script to scrape quotes, authors, and tags
├── analyze.py              # Script to clean data and generate analysis & plots
├── load_to_db.py           # Script to load data into SQLite database
├── query_db.py             # Script to query SQLite DB and display results
├── quotes.xlsx             # Raw scraped data saved in Excel format
├── quotes_clean.csv        # Cleaned CSV data after preprocessing
├── top_authors.png         # Bar chart of top authors by quote count
├── top_tags.png            # Bar chart of top tags by frequency
└── README.md               # Project documentation


Setup Instructions

Clone the repository

git clone <repository_url>
cd web_scraper_project


Create and activate virtual environment (optional but recommended)

python -m venv venv


Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate


Install dependencies

pip install requests beautifulsoup4 pandas matplotlib openpyxl sqlalchemy


Usage

Step 1: Scrape quotes data
Run the scraper to extract quotes, authors, and tags from the website and save them into an Excel file:

python scraper.py


This script scrapes all available pages and saves the output to quotes.xlsx.

Step 2: Analyze and clean data
Run the analysis script:

python analyze.py


This script:

Cleans and preprocesses scraped data

Generates summary statistics

Saves cleaned data as quotes_clean.csv

Creates visualizations (top_authors.png, top_tags.png)

Step 3: Load data into SQLite database
Run:

python load_to_db.py


This script:

Creates db/quotes.db SQLite database

Loads the quotes data into a table named quotes

Prints confirmation of inserted records

Step 4: Query the SQLite database
Run:

python query_db.py


This script:

Displays total quotes count

Shows top 5 authors

Shows top 10 most frequent tags

Sample SQL Queries Used

-- Total number of quotes
SELECT COUNT(*) FROM quotes;

-- Top 5 authors with most quotes
SELECT author, COUNT(*) AS count
FROM quotes
GROUP BY author
ORDER BY count DESC
LIMIT 5;

-- Top 10 tags
SELECT tags, COUNT(*) AS count
FROM quotes
GROUP BY tags
ORDER BY count DESC
LIMIT 10;


Notes

Ensure quotes.xlsx is closed before running load_to_db.py to avoid file lock issues.

The scraper uses polite delays to avoid overloading the website.

The db/ folder and quotes.db file are created automatically.

All generated charts are saved as PNG files in the project directory.

Dependencies

Python 3.7+
requests
beautifulsoup4
pandas
matplotlib
openpyxl
sqlalchemy

Author

Sowmyasri
B.Tech – Electrical & Electronics Engineering
