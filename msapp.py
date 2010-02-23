import nltk
import random
import re

def generate_model(cfd, cfdbi, w, num=15):
    
    txt = ""
    for i in range(num):
        
        #else:
            
        items = cfd[w].items()
      #  print "numitems " + str(len(items))
      
        if len(items) == 0:
       #     print "FALLBACK"
            items = cfdbi[w[1]].items()
            
        totalprob = sum(map(lambda (word, prob): prob, items))
        
        if totalprob <= 1:
            rint = 0
        else:
            rint = random.randint(0,totalprob-1)
       
        goOn = True

        for i in range(0,len(items)):
            if goOn:
                cursum = sum(map(lambda (word, prob): prob, items[:i]))

                if rint <= cursum:
                    theWord = items[i][0]
                    goOn = False
        
        punct = re.compile(r"[.:;,!?]")
        if punct.match(w[0]) is not None:
            txt += str(w[0])+"\n"
        else:
            txt += str(w[0])+" "
        w = (w[1], theWord)
    txt = re.sub(r' ([.:;,!?\'"])',r'\1',txt)
    txt = re.sub(r'\' ', '\'',txt)
    return txt

plwords = nltk.corpus.gutenberg.words('milton-paradise.txt')[:1000]
grams = nltk.util.trigrams(plwords)
bigrams = nltk.util.bigrams(plwords)
#print grams
cfd = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in grams])
cfdbi = nltk.ConditionalFreqDist(bigrams)
#print plwords.collocations()
print cfd[('what','is')].items()
tex = generate_model(cfd, cfdbi, ('what','is'), 1000)
print tex