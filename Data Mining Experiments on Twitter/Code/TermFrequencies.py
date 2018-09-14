from TextPreprocessing import preprocess
from nltk.corpus import stopwords
from collections import Counter
import json
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

fname = 'Tweets/stream_demonetisation.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        if tweet.get('text'):
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Update the counter
            count_all.update(terms_stop)
    # Print the first 5 most frequent words
    #print(count_all.most_common(5))
