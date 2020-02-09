import string
from collections import defaultdict

def read_file(path):
    f = open(path, "r")
    return f.read().splitlines()

def tokenize_sentence(sentence):
    """
    input : sentence in sting format
    output : list of tuples, (word, pos)
    """
    #remove the outer [[ ]] 
    sentence = sentence[2:-2]
    tokens = sentence.split("], [")
    processed_tokens = []
    for token in tokens:
        [word, pos]= token.split(", ")
        # remove quotations around each tokens
        processed_tokens.append((word[1:-1] ,pos[1:-1]))
    return processed_tokens

def tokenize_corpus(corpus, n):
    """
    input : corpus as list of sentences
    output : list of lists of tuples (word, pos)
    """
    processed_corpus = []
    for sentence in corpus:
        if n = 2:
            processed_corpus.append(["<START>"] + tokenize_sentence(sentence) + ["<STOP>"])
        if n = 3:
            processed_corpus.append(["<START1>", "<START2>"] + tokenize_sentence(sentence) + ["<STOP>"])
    return processed_corpus

def count_unigrams(corpus):
    unigram_count = defaultdict(int)
    for sentence in corpus:
        for word in sentence:
            unigram_count[word] += 1
    return unigram_count

def extract_vocab(unigram_count, min_count = 1):
    """
    input : defaultdict of unigrams : count
    output : defaultdict with unigrams of low frequency converted to <UNK> : count
    """
    vocab = defaultdict(int)
    for word, count in unigram_count.items():
        if count <= min_count:
            vocab[("<UNK>", word[1])] += min_count
        else: 
            vocab[word] = count
    return vocab, len(vocab)

def set_unk(corpus, vocab):
    """
    input: corpus, list of lists of tuples (word, pos)
    output: corpus with words not in vocab converted to UNK.  list of lists of tuples (<UNK>, pos)
    """
    new_corpus = []
    for sentence in corpus:
        new_sentence = []
        for word in sentence:
            if word not in vocab:
                word = ("<UNK>", word[1])
            new_sentence.append(word)
        new_corpus.append(new_sentence)
    return new_corpus

def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('','',string.punctuation))


