import praw
import pandas as pd
import matplotlib.pyplot as plt

# Reddit credentials (placeholder - assumed already set up in actual script)
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# Analyze subreddit
analyze_subreddit = reddit.subreddit("programming")
keywords = ["data structure", "distributed system"]
counts = {k: 0 for k in keywords}

# Count keyword occurrences in the titles of 500 new posts
for post in analyze_subreddit.new(limit=500):
    title = post.title.lower()
    for keyword in keywords:
        if keyword in title:
            counts[keyword] += 1

# Prepare data for visualization
df = pd.DataFrame(list(counts.items()), columns=["Topic", "Count"])
df["Percentage"] = (df["Count"] / df["Count"].sum()) * 100

# Plot
plt.figure(figsize=(6, 6))
plt.pie(df["Count"], labels=[f"{row['Topic']} ({row['Percentage']:.1f}%)" for _, row in df.iterrows()],
        autopct='%1.1f%%', startangle=140)
plt.title("Popularity Comparison: Data Structures vs Distributed Systems")
plt.axis('equal')

plt.tight_layout()
plt.show()
