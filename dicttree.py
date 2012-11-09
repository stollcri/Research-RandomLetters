#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, fileinput

def process_file():
	flattened_tree = [16, 8, 23, 4, 12, 20, 25, 2, 6, 10, 14, 18, 22, 24, 26, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
	letter_total = 0

	# read in the file and create a list of tuples with letters and counts
	letter_counts = []
	for line in fileinput.input():
		split_line = line.partition(" ")
		letter = split_line[0]
		count = int(split_line[2])

		letter_total += int(count)

		letter_tuple = letter, count
		letter_counts.append(letter_tuple)

	# sort the list of letter tuples from most frequent to least frequent
	letter_counts = sorted(letter_counts, key=lambda x: -x[1])

	# calculate each letters probability and record it to a new tuple list
	letter_percentages = []
	for index, letter_count in enumerate(letter_counts):
		letter_percent = round(float(letter_count[1]) / float(letter_total), 9)
		letter_position = flattened_tree[index]
		letter_tuple = letter_position, letter_count[0], letter_count[1], letter_percent
		letter_percentages.append(letter_tuple)

	# sort the list of letter tuples by its position in the flattened tree
	letter_percentages = sorted(letter_percentages, key=lambda x: x[0])

	# calculate the ranges for each letter based upon its probability
	letter_ranges = []
	number_line_marker = -0.000000001
	for letter_percent in letter_percentages:
		letter_range = letter_percent[3]
		letter_range_start = round(number_line_marker + 0.000000001, 9)
		number_line_marker = round(letter_range_start + letter_range - 0.000000001, 9)
		letter_tuple = letter_percent[1], letter_range, letter_range_start, number_line_marker
		letter_ranges.append(letter_tuple)

	# sort for building the tree
	letter_ranges = sorted(letter_ranges, key=lambda x: -x[1])

	for letter_range in letter_ranges:
		print letter_range

		
if __name__ == "__main__":
	if len(sys.argv) >= 2 and sys.argv[1] == "-?":
		print "Syntax: dicttree.py letterlist.txt"
	else:
		process_file()
