import praw

# Σύνδεση στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)


# Επιλογή subreddit για δοκιμές
subreddit = reddit.subreddit("test")

# Δημιουργία περιεχομένου post
title = "📊 Σύνοψη Δημοφιλών Θεμάτων Πληροφορικής στο Reddit"
body = (
    "Καλησπέρα Reddit!\n\n"
    " Σήμερα εντοπίστηκαν:\n"
    "- 123 posts για Python\n"
    "- 87 για Java\n"
    "- 51 για C++\n\n"
    "Δεδομένα αντλημένα αυτόματα μέσω του Reddit API.\n"
    "#bot #dataanalysis"
)

# Δημοσίευση
subreddit.submit(title, selftext=body)

print(" Το bot δημοσίευσε με επιτυχία.")
