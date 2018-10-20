import praw
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
reddit = praw.Reddit(client_id='jW52Y1LgB9macg',
                     client_secret='1AXsqJzF3__OS-MMmKK5bv7iO8g',
                     user_agent='bobispro4')
print(reddit.read_only)
all = ""
for submission in reddit.subreddit('wallstreetbets').top(limit=100):
    
    # submission.comments.replace_more(limit=None)
    # for comment in submission.comments.list():
    #     if(comment.author!="WSBVoteBot" and comment.author!="auto_moderator"):
    #         all+= comment.body
    submission.comments.replace_more(limit=None)
    for top_level_comment in submission.comments:
        all+=top_level_comment.body+" "
        for second_level_comment in top_level_comment.replies:
            all+=top_level_comment.body+ " "
            for third_level_comment in second_level_comment.replies:
                all+=top_level_comment.body+ " "
tokenized = word_tokenize(all)
print(tokenized.length)