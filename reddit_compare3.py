import praw
import matplotlib.pyplot as plt

# Σύνδεση στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Subreddit για ανάλυση
subreddit = reddit.subreddit("programming")

# Λέξεις-κλειδιά προς μέτρηση
keywords = ["python", "java", "html", "assembly"]
counts = {k: 0 for k in keywords}

# Τραβάμε 500 posts (από την κατηγορία "new")
for post in subreddit.new(limit=500):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counts[keyword] += 1

# Υπολογισμός ποσοστών
total = sum(counts.values())
percentages = {k: round((v / total) * 100, 1) for k, v in counts.items()}

# Γράφημα πίτας
plt.figure(figsize=(6, 6))
plt.pie(
    percentages.values(),
    labels=[f"{k.upper()} ({v}%)" for k, v in percentages.items()],
    autopct='%1.1f%%'
)
plt.title("Language Popularity on Reddit (without C)")
plt.show()

