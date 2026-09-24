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

# 2. LLM Summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 3. Reddit Post ID
post_id = "1ikj3ne"
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=0)

# 4. Λήψη και προεπεξεργασία σχολίων
comments = [c.body for c in submission.comments.list() if len(c.body) > 20][:30]
text = " ".join(comments)[:3500]

# 5. Δημιουργία σύνοψης
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
summary_text = summary[0]["summary_text"]

# 6. Δημοσίευση ως νέο post στο r/test
title = "📚 Σύνοψη σχολίων: Αγαπημένη γλώσσα προγραμματισμού (r/thinkpad)"
body = (
    f"Αναλύθηκαν τα 30 πρώτα σχόλια από το post:\n{submission.url}\n\n"
    f"📊 **Σύνοψη**:\n{summary_text}\n\n"
    "#reddit #nlp #dataanalysis"
)
reddit.subreddit("test").submit(title, selftext=body)
print("📰 Δημοσιεύτηκε νέο post με τη σύνοψη!")

# 7. Rate-limit friendly delay
print("⌛ Περιμένουμε 60 δευτερόλεπτα πριν το comment...")
time.sleep(60)

# 8. Δημοσίευση ως comment κάτω από το αρχικό post
comment_text = f"📚 **Σύνοψη σχολίων**:\n\n{summary_text}"
submission.reply(comment_text)
print("💬 Δημοσιεύτηκε σύνοψη ως σχόλιο!")
