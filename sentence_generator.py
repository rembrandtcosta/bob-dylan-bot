import nltk
import random
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import semcor

def create_corpus():
    corpus_root = './data'
    newcorpus = PlaintextCorpusReader(corpus_root, '.*')
    return newcorpus

def generate_random_sentence():
    nltk.download('punkt')
    corpus = create_corpus()
    max_sentence = len(corpus.sents())-1
    corpus_sentence = corpus.sents()[random.randint(0, max_sentence)]
    sentence = format_sentence(corpus_sentence)
    return sentence

def format_sentence(sentence):
    return TreebankWordDetokenizer().detokenize(sentence)

