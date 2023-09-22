#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mrjob.job import MRJob
import re

# List of stopwords
stopwords_list = set(["the", "and", "of", "a", "to", "in", "is", "it"])

WORD_RE = re.compile(r"\b\w+\b")

class NonStopWordCount(MRJob):

    def mapper(self, _, line):
        words = re.findall(WORD_RE, line.lower())
        for word in words:
            if word not in stopwords_list:
                yield (word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))


# In[ ]:


if __name__ == '__main__':
    NonStopWordCount.run()


# In[ ]:




