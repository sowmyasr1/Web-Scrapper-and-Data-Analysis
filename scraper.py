import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Headers to act like a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36"
}

base_url = "http://quotes.toscrape.com/page/{}/"
all_data = []

page = 1
while True:
    try:
        response = requests.get(base_url.format(page), headers=HEADERS, timeout=10)

        # Check if page exists
        if response.status_code != 200:
            print(f"❌ No more pages. Stopping at page {page}.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            print("✅ Reached last page.")
            break

        for q in quotes:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
            all_data.append({"Quote": text, "Author": author, "Tags": ", ".join(tags)})

        print(f"✅ Page {page} scraped successfully.")

        page += 1

        # Sleep randomly to avoid being blocked
        time.sleep(random.uniform(1, 3))

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error on page {page}: {e}")
        break

# Save data
df = pd.DataFrame(all_data)
df.to_excel("quotes.xlsx", index=False, engine="openpyxl")
print("🎉 Scraping complete! Data saved in quotes.xlsx")
