import praw
import time
from transformers import pipeline

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 🧠 Hugging Face summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 📌 Reddit Post ID (από το πρόσφατο post που επέλεξες)
post_id = "1hgau3p"
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=0)

# ✂️ Πάρε τα πρώτα 30 σχόλια
comments = [c.body for c in submission.comments.list()[:30]]
text = " ".join(comments)[:3500]  # κόβουμε σε ασφαλές όριο

# 🔮 Σύνοψη
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
summary_text = summary[0]["summary_text"]

# 🌍 Μετάφραση στα ελληνικά
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-el")
translated = translator(summary_text, max_length=400)[0]["translation_text"]

# 📰 Δημιουργία νέου post στο r/test
title = "📚 Σύνοψη απαντήσεων: Αγαπημένη γλώσσα προγραμματισμού στο Reddit"
body = (
    f"Αναλύθηκαν τα 30 πρώτα σχόλια από το παρακάτω post:\n"
    f"{submission.url}\n\n"
    f"📊 **Σύνοψη (στα ελληνικά)**:\n{translated}\n\n"
    "#reddit #nlp #dataanalysis"
)

reddit.subreddit("test").submit(title, selftext=body)
print("📰 Δημοσιεύτηκε νέο post με τη σύνοψη!")

# 💤 Rate-limit friendly delay
print("⌛ Περιμένουμε 60 δευτερόλεπτα πριν το comment για να μην φάμε block από Reddit...")
time.sleep(60)

# 💬 Δημοσίευση comment στο αρχικό post
comment_text = f"📚 **Σύνοψη απαντήσεων** (αυτόματη):\n\n{translated}"
submission.reply(comment_text)
print("💬 Δημοσιεύτηκε σύνοψη ως σχόλιο!")
