import praw
from collections import defaultdict
import matplotlib.pyplot as plt

# 🔐 Reddit API setup
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 📌 Subreddits to check
subreddits = ["learnprogramming", "programming", "webdev", "cscareerquestions", "compsci", "frontend", "coding"]

keyword_variants = ["backend", "back-end"]
mention_counts = {}

# 📊 Count keyword mentions
for sub in subreddits:
    count = 0
    subreddit = reddit.subreddit(sub)
    for post in subreddit.new(limit=500):
        title = post.title.lower()
        if any(keyword in title for keyword in keyword_variants):
            count += 1
    mention_counts[sub] = count

# 📈 Sorted plotting
sorted_items = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)
labels = [item[0] for item in sorted_items]
values = [item[1] for item in sorted_items]

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values)
plt.title("🔧 Backend Development Mentions in Subreddits")
plt.ylabel("Αναφορές (σε τίτλους post)")

for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.show()
