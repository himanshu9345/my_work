from nltk.corpus import stopwords
import string
import operator
import json
from nltk import bigrams
import nltk

from collections import Counter
import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


fname = 'india_tweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        punctuation = list(string.punctuation)
        if tweet.get('text'):
            terms_all = [term for term in preprocess(tweet['text'])]
            stop = stopwords.words('english') + punctuation + ['RT', 'via']
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            terms_single = set(terms_all)
            # Count hashtags only
            terms_hash = [term for term in preprocess(tweet['text'])
                          if term.startswith('#') and term not in stop]
            # Count terms only (no hashtags, no mentions)
            terms_only = [term for term in preprocess(tweet['text'])
                          if term not in stop and
                          not term.startswith(('#', '@'))]
            terms_bigram = bigrams(terms_stop)
            # mind the ((double brackets))
            # startswith() takes a tuple (not a list) if
            # we pass a list of inputs

            count_all.update(terms_only)

            # print(pairs)
    print(count_all.most_common(100))
