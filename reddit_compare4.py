import praw
from collections import Counter
import matplotlib.pyplot as plt

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Define keywords and counter
keywords = ["linux", "windows", "macos"]
counter = Counter()

# Search posts in target subreddit
subreddit = reddit.subreddit("programming")
for post in subreddit.new(limit=500):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counter[keyword] += 1

# Prepare data for pie chart
labels = []
sizes = []
for key in keywords:
    labels.append(key.capitalize())
    sizes.append(counter[key])

# Plot
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("OS Popularity in r/programming (based on post titles)")
plt.axis('equal')
plt.tight_layout()
plt.show()
