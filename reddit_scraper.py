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

# Subreddits για κάθε γλώσσα
subreddits = {
    "C": "C_Programming",
    "Java": "java",
    "Python": "Python"
}

# Αποθήκευση αριθμού posts
post_counts = {}

# Αυξάνουμε το όριο των posts
POST_LIMIT = 1000  # Από 100 σε 1000

# Ανάκτηση δεδομένων από κάθε subreddit
for lang, sub in subreddits.items():
    subreddit = reddit.subreddit(sub)
    posts = list(subreddit.hot(limit=POST_LIMIT))  # Παίρνουμε 1000 posts
    post_counts[lang] = len(posts)

# Δημιουργία γραφήματος
plt.bar(post_counts.keys(), post_counts.values(), color=['blue', 'red', 'green'])
plt.xlabel("Γλώσσα Προγραμματισμού")
plt.ylabel("Αριθμός Posts")
plt.title(f"Σύγκριση αριθμού δημοσιεύσεων στο Reddit (Δείγμα: {POST_LIMIT} posts/subreddit)")
plt.show()
