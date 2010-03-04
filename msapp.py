import nltk
import random
import re
from msfunctions import *
import news
import sys

def isVowel(phone):
    if re.search(r'[012]',phone) is not None:
        return 1
    else:
        return 0
        
def reg_upper(mo):
    return mo.group(0).upper()
    
def reg_lower_if(mo):
    w = mo.group(0).lower()
    if w[1:] in cmu_words:
        return mo.group(0).lower()
    else:
        return mo.group(0)
        
def generate(filename, instances, textlen):
    
    for n in range(instances):
    
        outp = generate_model(cfdtri, cfdbi, random.choice(bigrams), plwords, textlen)
    
        verses = ""
        line = ""
        line_sylls = 0
        for word in outp:
            if line_sylls >= 10 and re.match(r'[.:;,!?]',word) is not None:
                line += word
                line_sylls = 0
                verses += line + "\n"
                line = ""
                continue
            elif line_sylls >= 10:
                line_sylls = 0
                verses += line + "\n"
                line = ""
            if word.lower() in cmu_words:
                pronunc_l = cmu_dict[word.lower()]
                #print pronunc_l
                pronunc = pronunc_l[0]
                num_syllables = sum(map(isVowel, pronunc))
        #        print word + ": " + str(num_syllables)
                line_sylls += num_syllables
            elif len(word) > 1:
                num_syllables = int(round(len(word) / 2))
                line_sylls += num_syllables
      #          print word + "(g): " + str(num_syllables)
            line += word + " "
    
    
        verses = verses[0].upper() + verses[1:]
        verses = re.sub(r'\n([.:;,!?]) ',r'\1\n',verses)            #move punct at line beginnings up to prev line
        verses = re.sub(r' ([.:;,!?\'"])',r'\1',verses)             #remove spaces before punctuation
        verses = re.sub(r'\n.',reg_upper,verses)                    #uppercase line beginnings
        verses = re.sub(r' [A-Z][A-Za-z]+',reg_lower_if,verses)     #lowercase words that are in dict if not at line beginning
        verses = re.sub(r'[.!?] ([a-z])',reg_upper,verses)          #uppercase words after sentence end if not at line beginning
    
        if n == 0:
            print verses
   
        fi = open(str(filename) + "-" + str(n) + ".txt", 'w')
        fi.write(verses.decode("UTF-8").encode("UTF-16"))
        
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "news"

cmu_reader = nltk.corpus.cmudict
#print "building cmu dict..."
cmu_dict = cmu_reader.dict()
cmu_words = cmu_reader.words()


nsents = news.getNews()
nwords = []
for sent in nsents:
    lsent = sent.split(" ")
    nwords.extend(lsent)


plwords = []
plwords.extend(nltk.corpus.gutenberg.words('milton-paradise.txt')[20:1000])
plwords.extend(nwords)
grams = nltk.util.trigrams(plwords)
bigrams = nltk.util.bigrams(plwords)
cfdtri = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in grams])
cfdbi = nltk.ConditionalFreqDist(bigrams)
    
generate(filename, 1, 1000)
    
   


