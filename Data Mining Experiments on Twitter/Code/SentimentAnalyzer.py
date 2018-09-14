import math
import operator

from TermCooccurences import com,defaultdict,no_of_lines
from TermFrequencies import count_all


positive_vocab = [
    'good', 'nice', 'great', 'awesome', 'outstanding','fantastic', ':)', ':-)', 'like', 'love','triumph', 'triumphal', 'triumphant', 'victory'
]

negative_vocab = [
    'bad', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(','defeat'
]

# n_docs is the total n. of tweets
n_docs = no_of_lines; #change to write code to calculate no  of lines

p_t = {}
p_t_com = defaultdict(lambda: defaultdict(int))

for term, n in count_all.items():
    p_t[term] = n / n_docs
    for t2 in com[term]:
        p_t_com[term][t2] = com[term][t2] / n_docs

pmi = defaultdict(lambda: defaultdict(int))
for t1 in p_t:
    for t2 in com[t1]:
        denom = p_t[t1] * p_t[t2]
        pmi[t1][t2] = math.log2(p_t_com[t1][t2] / denom)

semantic_orientation = {}
for term, n in p_t.items():
    positive_assoc = sum(pmi[term][tx] for tx in positive_vocab)
    negative_assoc = sum(pmi[term][tx] for tx in negative_vocab)
    semantic_orientation[term] = positive_assoc - negative_assoc

semantic_sorted = sorted(semantic_orientation.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
top_pos = semantic_sorted[:20]
top_neg = semantic_sorted[-20:]

print(top_pos)
print(top_neg)