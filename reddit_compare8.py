import praw
from collections import defaultdict
import matplotlib.pyplot as plt

# Ρύθμιση σύνδεσης στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Subreddit για ανάλυση
subreddit = reddit.subreddit("learnprogramming")

# Θέματα προς σύγκριση
keywords = {
    "DevOps": ["devops", "ci/cd", "docker"],
    "Cyber Security": ["cybersecurity", "security", "infosec"]
}

counts = defaultdict(int)

# Ανάκτηση τίτλων
for post in subreddit.new(limit=1000):
    title = post.title.lower()
    for topic, keys in keywords.items():
        if any(key in title for key in keys):
            counts[topic] += 1

# Δημιουργία γραφήματος
labels = list(counts.keys())
values = list(counts.values())

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("DevOps vs Cyber Security (Reddit Mentions)")
plt.tight_layout()
plt.savefig("devops_vs_cybersecurity.png")
plt.show()
