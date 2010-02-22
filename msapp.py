import nltk

def generate_model(cfd, w, num=15):
    for i in range(num):
        if w[1] == None:
            print ''
        elif w[1] == '.' or w[1] == ',' or w[1] == ';':
            print w[1]
        else:
            print w[1],
        w = (w[1], cfd[w].max())

plwords = nltk.corpus.gutenberg.words('milton-paradise.txt')[:5000]
grams = nltk.util.trigrams(plwords)
#print grams
cfd = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in grams])
#print plwords.collocations()
#print cfd[('what','is')]
generate_model(cfd, ('what','is'), 100)