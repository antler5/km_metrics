from enum import Enum

NgramType = Enum("NgramType", ["MONOGRAM", "BIGRAM", "SKIPGRAM", "TRIGRAM"])
    
class Metric:
    def __init__(self, name, short, ngram_type, predicate, value):
        self.name = name
        self.short = short
        self.ngram_type = ngram_type
        self.predicate = predicate
        self.value = value
