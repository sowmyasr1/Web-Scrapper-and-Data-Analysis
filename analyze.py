import pandas as pd
import matplotlib.pyplot as plt

# 1) Load scraped data
df = pd.read_excel("quotes.xlsx")

# 2) Basic cleaning & helpful columns
df["Quote"] = df["Quote"].astype(str).str.strip()
df["Author"] = df["Author"].astype(str).str.strip()
df["Tags"] = df["Tags"].fillna("").astype(str)

# new helper columns
df["word_count"] = df["Quote"].str.split().apply(len)
df["tag_count"] = df["Tags"].apply(lambda s: 0 if s.strip()=="" else len([t for t in s.split(", ") if t]))

# 3) Save a cleaned CSV for your repo/resume
df.to_csv("quotes_clean.csv", index=False, encoding="utf-8")
print("✅ Saved cleaned data -> quotes_clean.csv")

# 4) Simple insights (printed)
print("\n— STATS —")
print("Total quotes:", len(df))
print("Average words per quote:", round(df["word_count"].mean(), 2))

top_authors = df["Author"].value_counts().head(5)
print("\nTop 5 authors by number of quotes:\n", top_authors)

# explode tags for counts
tags_series = df["Tags"].str.split(", ").explode()
tags_series = tags_series[tags_series.str.len() > 0]  # drop empties
top_tags = tags_series.value_counts().head(10)
print("\nTop 10 tags:\n", top_tags)

# 5) Optional charts (saved as PNGs)
plt.figure()
top_authors.plot(kind="bar", title="Top 5 Authors by Quote Count")
plt.xlabel("Author"); plt.ylabel("Quotes"); plt.tight_layout()
plt.savefig("top_authors.png")

plt.figure()
top_tags.plot(kind="bar", title="Top 10 Tags")
plt.xlabel("Tag"); plt.ylabel("Count"); plt.tight_layout()
plt.savefig("top_tags.png")

print("\n📊 Charts saved: top_authors.png, top_tags.png")