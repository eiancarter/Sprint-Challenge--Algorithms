'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
from collections import Counter

def count_th(word):
    if len(word) <= 1:
        return 0
    # elif word == 'th': ## this seems redundant
    #     return 1
    if word[0:2] == 'th':
        return 1 + count_th(word[2 - 1:])
    else:
        return count_th(word[2 -1:])

