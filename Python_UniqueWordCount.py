#!/usr/bin/env python
# coding: utf-8

# In[11]:


from mrjob.job import MRJob
import re

word_re = re.compile(r"\w+")

class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in word_re.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


# In[12]:


if __name__ == '__main__':
    MRWordCount.run()


# In[ ]:





# In[ ]:





# In[ ]:




