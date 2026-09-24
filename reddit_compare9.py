import praw
from collections import defaultdict
import matplotlib.pyplot as plt

# Reddit API credentials (θα χρησιμοποιηθούν από το περιβάλλον σου)
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Subreddit για ανάλυση
subreddit = reddit.subreddit("learnprogramming")

# Λέξεις-κλειδιά ανά θεματική
keywords = {
    "Data Structures": ["data structures", "linked list", "binary tree", "heap", "stack", "queue"],
    "Machine Learning": ["machine learning", "ml", "neural network", "deep learning", "supervised", "unsupervised"]
}

# Ανάλυση post titles
counts = defaultdict(int)
for post in subreddit.new(limit=1000):
    title = post.title.lower()
    for category, terms in keywords.items():
        if any(term in title for term in terms):
            counts[category] += 1

# Δεδομένα για το γράφημα
labels = list(counts.keys())
values = list(counts.values())

# Ποσοστά
total = sum(values)
percentages = [f"{v/total*100:.1f}%" for v in values]

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=[f"{l} ({p})" for l, p in zip(labels, percentages)], autopct='%1.1f%%', startangle=90)
plt.title("Data Structures vs Machine Learning (Reddit Mentions)")
plt.axis('equal')
plt.tight_layout()
plt.savefig("data_structures_vs_ml.png")
plt.show()
