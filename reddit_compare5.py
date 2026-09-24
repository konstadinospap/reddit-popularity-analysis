import praw
import matplotlib.pyplot as plt
from collections import defaultdict

# 🔑 Reddit API credentials
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 🎯 Subreddit για ανάλυση
analyze_subreddit = reddit.subreddit("webdev")  # Μπορείς να το αλλάξεις π.χ. σε "programming", "learnprogramming" κλπ

# 📊 Καταμέτρηση όρων
counts = defaultdict(int)

# 🧠 Λογική μέτρησης με αμοιβαίο αποκλεισμό
for post in analyze_subreddit.new(limit=1500):
    title = post.title.lower()
    if ("frontend" in title or "front-end" in title) and not ("backend" in title or "back-end" in title):
        counts["Frontend"] += 1
        print("FRONTEND:", title)
    elif ("backend" in title or "back-end" in title) and not ("frontend" in title or "front-end" in title):
        counts["Backend"] += 1
        print("BACKEND:", title)

# 💯 Υπολογισμός ποσοστών
total = sum(counts.values())
labels = list(counts.keys())
sizes = [round((v / total) * 100, 1) for v in counts.values()]

# 📈 Δημιουργία γραφήματος
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=[f"{l} ({s}%)" for l, s in zip(labels, sizes)], autopct='%1.1f%%', startangle=90)
plt.title("Frontend vs Backend Popularity on Reddit")
plt.axis('equal')
plt.tight_layout()
plt.savefig("frontend_vs_backend.png")
plt.show()
