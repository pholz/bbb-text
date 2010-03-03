import nltk
import random
import re

def generate_model(cfd, cfdbi, w, words, num=15):
    
    txt = []
    for i in range(num):
        
    #    print str(w)
            
        items = cfd[w].items()
      #  print "numitems " + str(len(items))
      
      
        bitems = cfdbi[w[1]].items()
        
        if len(items) == 0:
    #        print "FALLBACK: " + str(w)
            items = cfdbi[w[1]].items()
            
        totalprob = sum(map(lambda (word, prob): prob * 5, items))
        totalprob += sum(map(lambda (word, prob): prob, bitems))
        
        if totalprob <= 1:
            rint = 0
        else:
            rint = random.randint(0,totalprob-1)
       
        theWord = random.choice(words)
       
        goOn = True

        for i in range(0,len(items)):
            if goOn:
                cursum = sum(map(lambda (word, prob): prob * 5, items[:i]))

                if rint <= cursum:
                    theWord = items[i][0]
                    goOn = False
        if goOn:
            tempsum = sum(map(lambda (word, prob): prob * 5, items))
            for i in range(0,len(bitems)):
                if goOn:
                    cursum = tempsum + sum(map(lambda (word, prob): prob, bitems[:i]))

                    if rint <= cursum:
                        theWord = bitems[i][0]
                        goOn = False
        
        punct = re.compile(r"[.:;,!?]")
    #    if punct.match(w[0]) is not None:
    #        txt += str(w[0])+"\n"
    #    else:
        txt.append(str(w[0]))
        w = (w[1], theWord)
    
    return txt