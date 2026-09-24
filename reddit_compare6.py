import praw
from collections import defaultdict
import matplotlib.pyplot as plt

# 🔧 Reddit API setup
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 📌 Subreddit για ανάλυση
subreddit = reddit.subreddit("programming")

# 🔍 Όροι που θα αναζητήσουμε
keywords = {
    "software engineering": ["software engineering", "software engineer", "sw eng"],
    "data science": ["data science", "data scientist", "ds role"]
}

counts = defaultdict(int)

# 📥 Ανάλυση των post τίτλων
for post in subreddit.new(limit=1000):
    title = post.title.lower()
    for category, terms in keywords.items():
        if any(term in title for term in terms):
            counts[category] += 1

# 🎯 Εμφάνιση αποτελεσμάτων
labels = list(counts.keys())
values = list(counts.values())
percentages = [f"{(v / sum(values)) * 100:.1f}%" for v in values]

plt.figure(figsize=(6, 6))
plt.pie(values, labels=[f"{l} ({p})" for l, p in zip(labels, percentages)], autopct='%1.1f%%', startangle=140)
plt.title("Software Engineering vs Data Science (Reddit Analysis)")
plt.tight_layout()
plt.show()
