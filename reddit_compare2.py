import praw
import matplotlib.pyplot as plt

# 🔐 Reddit credentials
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 🔍 Λέξεις-κλειδιά
languages = ["c", "python", "java", "html", "assembly"]
counts = {lang: 0 for lang in languages}

# 📥 Ανάλυση subreddit
subreddit = reddit.subreddit("programming")
for post in subreddit.new(limit=500):
    title = post.title.lower()
    for lang in languages:
        if lang in title:
            counts[lang] += 1

# 📊 Ποσοστά
total = sum(counts.values())
percentages = {lang: (count / total) * 100 for lang, count in counts.items()}

# 📈 Πλοτ
plt.figure(figsize=(8, 6))
bars = plt.bar(
    [lang.upper() for lang in percentages.keys()],
    percentages.values()
)

# 🔢 Εμφάνιση ποσοστών πάνω από τις μπάρες
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f'{height:.1f}%',
        ha='center',
        va='bottom'
    )

plt.title("📊 Language Popularity on Reddit (Live Search)")
plt.ylabel("Percentage (%)")
plt.xlabel("Language")
plt.ylim(0, max(percentages.values()) + 10)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
