import praw
from collections import defaultdict
import matplotlib.pyplot as plt

# 🔐 Σύνδεση στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 🎯 Subreddit για ανάλυση
subreddit = reddit.subreddit("technology")  # μπορείς να αλλάξεις αν θες

# 🧠 Λέξεις-κλειδιά
keywords = ["software", "hardware"]
counts = defaultdict(int)

# 📥 Ανάλυση τίτλων από τα 1000 πιο πρόσφατα posts
for post in subreddit.new(limit=1000):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counts[keyword] += 1

# 📊 Υπολογισμός ποσοστών
total = sum(counts.values())
percentages = {k: (v / total) * 100 for k, v in counts.items()}

# 🎨 Pie chart
plt.figure(figsize=(6, 6))
plt.pie(percentages.values(), labels=percentages.keys(), autopct="%1.1f%%", startangle=90)
plt.title("Software vs Hardware Popularity on Reddit")
plt.axis("equal")
plt.tight_layout()
plt.savefig("software_vs_hardware.png")
plt.show()
