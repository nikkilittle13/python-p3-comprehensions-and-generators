#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [n for n in num_list if n % 2 == 0]
    return new_list
    pass

def make_exclamation(sentence_list):
    if sentence_list.count == 0:
        return []
    else:
        new_sentence_list = [word + '!' for word in sentence_list]
        return new_sentence_list
    pass