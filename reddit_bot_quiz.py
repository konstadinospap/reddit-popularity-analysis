import praw
import random
import time

# Σύνδεση στο Reddit API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)


# Subreddit για ανάλυση και για post
analyze_subreddit = reddit.subreddit("programming")
post_subreddit = reddit.subreddit("test")

# Επιλογές τεχνολογιών για quiz
all_techs = ["python", "java", "c++"]
chosen = random.sample(all_techs, 3)  # Random 3 επιλογές
counts = {k: 0 for k in chosen}

# Ανάλυση τελευταίων 500 posts
for post in analyze_subreddit.new(limit=500):
    title = post.title.lower()
    for tech in chosen:
        if tech in title:
            counts[tech] += 1

# Εύρεση σωστής απάντησης
correct = max(counts, key=counts.get)

# ✅ Post το quiz
title = "🤔 Daily Reddit Tech Trivia!"
body = (
    f"📌 Σήμερα στο r/programming, ποια τεχνολογία είχε τα περισσότερα posts;\n\n"
    f"A) {chosen[0].capitalize()}\n"
    f"B) {chosen[1].capitalize()}\n"
    f"C) {chosen[2].capitalize()}\n\n"
    "Σχολίασε την απάντησή σου 👇 Η σωστή απάντηση θα αποκαλυφθεί σύντομα!"
)

quiz_post = post_subreddit.submit(title, selftext=body)
print("📮 Quiz δημοσιεύτηκε.")

# 🕐 Περιμένουμε 45 δευτερόλεπτα για "δράμα"
time.sleep(45)

# ✏️ Σχολιάζουμε τη σωστή απάντηση
answer_text = (
    f"✅ Η σωστή απάντηση είναι: **{correct.capitalize()}** με {counts[correct]} posts σήμερα!\n\n"
    "📊 Αναλυτικά:\n"
)
for tech in chosen:
    answer_text += f"- {tech.capitalize()}: {counts[tech]}\n"

answer_text += "\nΤα λέμε αύριο με νέο quiz! 🧠"

quiz_post.reply(answer_text)
print("✅ Απάντηση σχολιάστηκε με επιτυχία.")
