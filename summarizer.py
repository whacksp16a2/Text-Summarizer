from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 2

def getSummary(parser, sentences_count):
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    sentences = []
    for sentence in summarizer(parser.document, sentences_count):
        sentences.append(sentence)

    return sentences

def getSummaryFromWebsite(url, sentences_count):

    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

    return getSummary(parser, sentences_count)

def getSummaryFromFile(path, sentences_count):

    parser = PlaintextParser.from_file(path, Tokenizer(LANGUAGE))

    return getSummary(parser, sentences_count)

if __name__ == "__main__":
    path = "BookThief.txt"
    sentences = getSummaryFromFile(path, SENTENCES_COUNT)
    map(print, sentences)
