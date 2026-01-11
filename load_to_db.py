# load_to_db.py
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# 1) Ensure the DB folder exists
db_dir = Path("db")
db_dir.mkdir(exist_ok=True)
db_path = db_dir / "quotes.db"

# 2) Read the Excel we created earlier
#    ⚠️ Close quotes.xlsx in Excel before running this script
df = pd.read_excel("quotes.xlsx")

# 3) Create SQLite engine and write table
engine = create_engine(f"sqlite:///{db_path}")
df.to_sql("quotes", con=engine, if_exists="replace", index=False)

# 4) Run a couple of verification queries
with engine.connect() as conn:
    total = conn.execute(text("SELECT COUNT(*) FROM quotes")).scalar()

    top_authors = conn.execute(text("""
        SELECT Author, COUNT(*) as cnt
        FROM quotes
        GROUP BY Author
        ORDER BY cnt DESC
        LIMIT 5
    """)).fetchall()

print(f"✅ Loaded {total} rows into {db_path} (table: quotes)")

print("\nTop 5 authors (by number of quotes):")
for author, cnt in top_authors:
    print(f" - {author}: {cnt}")