#!/usr/bin/env python3

"""
This script creates a reverse dictionary - a dictionary in which words
are arranged in alphabetical order not by initial, but by final letters,
and are aligned not to the left, but to the right.
Source wordlist is the "be_BY.dic"
Result dictionary is the "be_BY.reversed.txt" file.

"""

import locale
locale.setlocale(locale.LC_COLLATE, "be_BY.UTF-8")

def reverse_slicing(word):
    return word[::-1]

def wordlist_align():
    max_word = max(wordlist_prereversed, key=len)
    max_len = len(max_word)
    return max_len

# 1st reverse wordlist
with open("be_BY.dic", 'r', encoding='utf-8') as file_orig:
    wordlist_prereversed = [reverse_slicing(line) for line in file_orig]
wordlist_rows = len(wordlist_prereversed)
max_len = wordlist_align()
print('Prereverse complete')

# Sort reversed wordlist
wordlist_sorted = sorted(wordlist_prereversed, key=locale.strxfrm)
print('Sort complete')

# Final reverse sorted wordlist
wordlist_reversed = [reverse_slicing(word).rjust(max_len) for word in wordlist_sorted]

# Write reversed wordlist to file
with open("be_BY.reversed.txt","w", encoding='utf-8') as file_reversed:
    file_reversed.write(str(wordlist_rows) + ' словаформаў\n')
    file_reversed.writelines(wordlist_reversed)
print('Dictionary Reversed!!!')
