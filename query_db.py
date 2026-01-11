from sqlalchemy import create_engine, text
import pandas as pd

# Connect to SQLite database
engine = create_engine("sqlite:///db/quotes.db")

# 1. Total number of quotes
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM quotes"))
    print("Total Quotes:", result.scalar())

# 2. Top 5 authors with most quotes
query = """ 
SELECT author, COUNT(*) as count
FROM quotes
GROUP BY author
ORDER BY count DESC
LIMIT 5
"""
df_authors = pd.read_sql(query, engine)
print("\nTop 5 Authors:\n", df_authors)

# 3. Most common tags
query = """
SELECT tags, COUNT(*) as count
FROM quotes
GROUP BY tags
ORDER BY count DESC
LIMIT 10
"""
df_tags = pd.read_sql(query, engine)
print("\nTop 10 Tags:\n", df_tags)