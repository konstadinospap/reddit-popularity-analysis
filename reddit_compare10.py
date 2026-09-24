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

# Subreddit
subreddit = reddit.subreddit("all")

# Λέξεις-κλειδιά
terms = ["pastry", "chord"]
counts = {term: 0 for term in terms}

# Σάρωση τίτλων
for post in subreddit.new(limit=1000):
    title = post.title.lower()
    for term in terms:
        if term in title:
            counts[term] += 1

# Αν δεν βρέθηκε τίποτα
if sum(counts.values()) == 0:
    print("⚠️ Δεν βρέθηκαν σχετικά posts με τις λέξεις-κλειδιά. Δοκίμασε με άλλα terms.")
else:
    # Υπολογισμός ποσοστών
    total = sum(counts.values())
    percentages = {k: (v / total * 100) for k, v in counts.items()}

    # Γράφημα
    labels = [f"{k} ({percentages[k]:.1f}%)" for k in counts]
    sizes = list(counts.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Pastry vs Chord στο Reddit (σε 1000 νέα posts)")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

