#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def process_file(file_name):
	alphabet = {
		'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
		'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
		'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
		'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
		'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
		'z': 0
	}
	with open(file_name) as dictionary_file:
		for line in dictionary_file:
			for char in line:
				if char.lower() in alphabet:
					alphabet[char.lower()] = alphabet[char.lower()] + 1

	for letter in alphabet:
		print letter, alphabet[letter]

if __name__ == "__main__":
	if len(sys.argv) == 2:
		process_file(sys.argv[1])
	else:
		print "Syntax: dictstat.py wordlist.txt"
		print " prints statistical information from word list"