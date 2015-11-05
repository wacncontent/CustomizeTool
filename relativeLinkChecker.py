import re
from os.path import isfile
from setting import setting
link_reg = r'/documentation/articles/(?P<article>[\w|\-]+)/?'

def checkRelativeLink(text):
    text = removeComment(text)
    articles = list(set(re.findall(link_reg, text)))
    for article in articles:
        if not isfile(setting["815path"]+"articles/"+article+".md"):
            print("Warning: "+article+".md is not in 815")


def removeComment(text):
    while True:
        try:
            i = text.index("<!--")
            j = text[i:].index("-->")
            text = text.replace(text[i:i+j], "")
        except Exception:
            return text