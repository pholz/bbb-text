import nltk
import random
from msfunctions import *

if False:
    plwords = nltk.corpus.gutenberg.words('milton-paradise.txt')#[:1000]
    grams = nltk.util.trigrams(plwords)
    bigrams = nltk.util.bigrams(plwords)
    #print grams
    cfdtri = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in grams])
    cfdbi = nltk.ConditionalFreqDist(bigrams)
    #print plwords.collocations()
    #print cfd[('what','is')].items()
    tex = generate_model(cfdtri, cfdbi, random.choice(bigrams), 1000)
    print tex

convwords = nltk.corpus.nps_chat.words('10-19-20s_706posts.xml')[:80]
c_grams = nltk.util.trigrams(convwords)
c_bigrams = nltk.util.bigrams(convwords)
#print grams
c_cfdtri = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in c_grams])
c_cfdbi = nltk.ConditionalFreqDist(c_bigrams)
c_tex = generate_model(c_cfdtri, c_cfdbi, random.choice(c_bigrams), 1000)
print c_tex
