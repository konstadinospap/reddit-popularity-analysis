import praw

# Σύνδεση στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)


# Subreddit για ανάλυση και δημοσίευση
analyze_subreddit = reddit.subreddit("programming")  # ή cs, compsci, whatever
post_subreddit = reddit.subreddit("test")

# Λέξεις-κλειδιά που ψάχνουμε
keywords = ["python", "java", "c++"]
counts = {k: 0 for k in keywords}

# Τραβάμε 500 posts (π.χ. hot ή new)
for post in analyze_subreddit.new(limit=500):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counts[keyword] += 1

# Δημιουργία περιεχομένου post
title = "📊 Σύνοψη Δημοφιλών Θεμάτων Πληροφορικής στο Reddit"
body = "Καλησπέρα Reddit!\n\nΣήμερα εντοπίστηκαν:\n"

for keyword, count in counts.items():
    body += f"- {count} posts για {keyword.capitalize()}\n"

body += "\nΔεδομένα αντλημένα αυτόματα μέσω του Reddit API.\n#bot #dataanalysis"

# Δημοσίευση στο test
post_subreddit.submit(title, selftext=body)
print("✅ Το bot δημοσίευσε δυναμικά δεδομένα με επιτυχία.")
