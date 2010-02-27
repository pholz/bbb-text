import nltk

from nltk import load_parser


plsents = nltk.corpus.gutenberg.sents('milton-paradise.txt')
parser = load_parser('grammars/book_grammars/drt.fcfg', logic_parser=nltk.DrtParser())
trees = parser.nbest_parse(plsents[50])
print trees[0].node['SEM'].simplify()