import praw
import csv
import os
from datetime import datetime

# Σύνδεση στο Reddit API χρησιμοποιώντας Secrets
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Subreddit για ανάλυση και δημοσίευση
analyze_subreddit = reddit.subreddit("programming")
post_subreddit = reddit.subreddit("test")

# Λέξεις-κλειδιά που ψάχνουμε
keywords = ["python", "java", "c++", "c#", "javascript", "php", "matlab", "html"]
counts = {k: 0 for k in keywords}

# Ανάλυση 500 posts
for post in analyze_subreddit.new(limit=500):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counts[keyword] += 1

# 📅 Ημερομηνία για το αρχείο CSV
today = datetime.now().strftime("%Y-%m-%d")

# 📄 Καταγραφή σε CSV αρχείο
csv_file = "language_stats.csv"
file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    if not file_exists:
        writer.writerow(["Ημερομηνία"] + [kw.capitalize() for kw in keywords])
    writer.writerow([today] + [counts[kw] for kw in keywords])

# 📤 Δημιουργία post στο Reddit
title = "📊 Σύνοψη Δημοφιλών Θεμάτων Πληροφορικής στο Reddit"
body = "Καλησπέρα Reddit!\n\nΣήμερα εντοπίστηκαν:\n"
for keyword, count in counts.items():
    body += f"- {count} posts για {keyword.capitalize()}\n"
body += "\nΔεδομένα αντλημένα αυτόματα μέσω του Reddit API.\n#bot #dataanalysis"

# 📬 Δημοσίευση στο subreddit
post_subreddit.submit(title, selftext=body)
print("✅ Το bot δημοσίευσε δυναμικά δεδομένα με επιτυχία και τα αποθήκευσε στο CSV.")
