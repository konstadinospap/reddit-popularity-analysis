import praw
import matplotlib.pyplot as plt

# Reddit API σύνδεση
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Λίστα subreddits και λέξη-κλειδί
subreddits = ["learnpython", "python", "learnprogramming", "datascience", "programming", "MachineLearning", "coding", "deeplearning", "AskProgramming"]
keyword = "python"

# Συλλογή αναφορών
mention_counts = {}
for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    count = 0
    for post in subreddit.new(limit=200):
        if keyword.lower() in post.title.lower():
            count += 1
    mention_counts[sub] = count

# Ταξινόμηση φθίνουσα
sorted_items = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)
subreddits_sorted = [item[0] for item in sorted_items]
counts_sorted = [item[1] for item in sorted_items]

# Γράφημα
plt.figure(figsize=(12, 6))
bars = plt.bar(subreddits_sorted, counts_sorted)
plt.title(f"📊 Posts που περιέχουν τη λέξη '{keyword}' ανά Subreddit", fontsize=14)
plt.xlabel("Subreddit")
plt.ylabel("Αριθμός Αναφορών")

# Προσθήκη αριθμών στις μπάρες
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, int(yval), ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
