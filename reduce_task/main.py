import functools


def accumulate(doc, sentence):
    return doc + ". " + sentence


def accumulate_first_sentences(sentences, n):
    if not sentences or n < 1:
        return ""
    else:
        return functools.reduce(accumulate, sentences[:n]) + "."
