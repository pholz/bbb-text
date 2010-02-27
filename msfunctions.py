import nltk
import random
import re

def generate_model(cfd, cfdbi, w, num=15):
    
    txt = ""
    for i in range(num):
        
        print str(w)
            
        items = cfd[w].items()
      #  print "numitems " + str(len(items))
      
        if len(items) == 0:
            print "FALLBACK: " + str(w)
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