import nltk
import random
import re
from msfunctions import *

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

#cmu_reader = nltk.corpus.reader.cmudict.CMUDictCorpusReader(".",nltk.corpus.cmudict.fileids())#["cmudict.0.6d.txt"])
cmu_reader = nltk.corpus.cmudict
print "building cmu dict..."
cmu_dict = cmu_reader.dict()
cmu_words = cmu_reader.words()
#print cmu_dict
#print cmu_reader.entries()[100:200]

if True:
    plwords = nltk.corpus.gutenberg.words('milton-paradise.txt')[:1000]
    grams = nltk.util.trigrams(plwords)
    bigrams = nltk.util.bigrams(plwords)
    #print grams
    cfdtri = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in grams])
    cfdbi = nltk.ConditionalFreqDist(bigrams)
    
   # wset = set(plwords)
    for cd in cfdtri.conditions():
        print str(cd) + " - " + str(cfdtri[cd].items())
            
    outp = generate_model(cfdtri, cfdbi, random.choice(bigrams), plwords, 1000)
 #   print outp
    verses = ""
    
    line = ""
    line_sylls = 0
   # print outp
    for word in outp:
        if line_sylls >= 8 and re.match(r'[.:;,!?]',word) is not None:
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
    
    print verses
    # kill spaces before puncutation
#    tex = re.sub(r' ([.:;,!?\'"])',r'\1',outp)
    # line braks on punctuation
  #  tex = re.sub(r'([.,;])',r'\1\n',tex)
    # kill spaces after apostrophes
#    tex = re.sub(r'\' ', '\'',tex)
#    print tex

if False:
    convwords = nltk.corpus.nps_chat.words('10-19-20s_706posts.xml')[:80]
    c_grams = nltk.util.trigrams(convwords)
    c_bigrams = nltk.util.bigrams(convwords)
    #print grams
    c_cfdtri = nltk.ConditionalFreqDist([((w1,w2),w3) for (w1, w2, w3) in c_grams])
    c_cfdbi = nltk.ConditionalFreqDist(c_bigrams)
    c_tex = generate_model(c_cfdtri, c_cfdbi, random.choice(c_bigrams), plwords, 1000)
    print c_tex
