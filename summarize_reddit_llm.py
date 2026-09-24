import praw
from transformers import pipeline

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"]
)

# 🎯 Post ID από Reddit link
post_id = "117q6at"
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=0)

# 🧹 Πάρε τα πρώτα 30 σχόλια
comments = [c.body for c in submission.comments.list()[:30]]
text = " ".join(comments)

# ✂️ Κρατάμε μέχρι 1024 tokens περίπου (~3500 χαρακτήρες) λόγω περιορισμού μοντέλου
text = text[:3500]

# 🧠 Φόρτωσε summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 🔮 Σύνοψη
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

# ✅ Εκτύπωσε αποτέλεσμα
print("\n📊 ΣΥΝΟΨΗ ΣΧΟΛΙΩΝ:\n")
print(summary[0]['summary_text'])
