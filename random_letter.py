#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random

class BTNode:
	nval = ""
	nmin = 0.0
	nmax = 1.0
	left = None
	right = None

	def __init__(self, data):
		self.nval = data["nval"]
		self.nmin = data["nmin"]
		self.nmax = data["nmax"]
		self.left = None
		self.right = None

class BTree:
	def __init__(self):
		self.root = None

	def addNode(self, data):
		return BTNode(data)

	def insert(self, root, data):
		if root == None:
			return self.addNode(data)
		else:
			if data["nmax"] <= root.nmin:
				root.left = self.insert(root.left, data)
			else:
				root.right = self.insert(root.right, data)
			return root
			
	def lookup(self, root, value):
		if root == None:
			return False
		else:
			#print root.nval, root.nmin, root.nmax
			if value < root.nmax and value > root.nmin:
				return root.nval
			else:
				if value > root.nmax:
					return self.lookup(root.right, value)
				else:
					return self.lookup(root.left, value)



def pick_a_letter(letter_count):
	letter_list = [
		('e', 0.105022804, 0.538979491, 0.644002294),
		('i', 0.089845073, 0.267441153, 0.357286225),
		('a', 0.088258618, 0.785527013, 0.873785630),
		('o', 0.076191970, 0.105176925, 0.181368894),
		('r', 0.071804464, 0.418384245, 0.490188708),
		('n', 0.070815226, 0.682697737, 0.753512962),
		('t', 0.067765522, 0.903911257, 0.971676778),
		('s', 0.061441654, 0.023092087, 0.084533740),
		('l', 0.057969911, 0.198858882, 0.256828792),
		('c', 0.045225401, 0.366164283, 0.411389683),
		('u', 0.039043109, 0.496249139, 0.535292247),
		('p', 0.033992527, 0.647066784, 0.681059310),
		('m', 0.030812000, 0.754715013, 0.785527012),
		('d', 0.030125626, 0.873785631, 0.903911256),
		('h', 0.028323223, 0.971676779, 1.000000001),
		('y', 0.023092087, 0.000000000, 0.023092086),
		('g', 0.020643184, 0.084533741, 0.105176924),
		('b', 0.017489987, 0.181368895, 0.198858881),
		('f', 0.010612360, 0.256828793, 0.267441152),
		('v', 0.008878057, 0.357286226, 0.366164282),
		('k', 0.006994561, 0.411389684, 0.418384244),
		('w', 0.006060430, 0.490188709, 0.496249138),
		('z', 0.003687243, 0.535292248, 0.538979490),
		('x', 0.003064489, 0.644002295, 0.647066783),
		('q', 0.001638426, 0.681059311, 0.682697736),
		('j', 0.001202050, 0.753512963, 0.754715012)
	]

	binary_tree = BTree()
	tree_root = binary_tree.addNode({
		"nval": letter_list[0][0], "nmin": letter_list[0][2], "nmax": letter_list[0][3]})
	for x in xrange(1, len(letter_list)):
		binary_tree.insert(tree_root, {
			"nval": letter_list[x][0], "nmin": letter_list[x][2], "nmax": letter_list[x][3]})

	for x in xrange(letter_count):
		print binary_tree.lookup(tree_root, random.random()),


if __name__ == "__main__":
	if len(sys.argv) == 2:
		pick_a_letter(int(sys.argv[1]))
	else:
		pick_a_letter(1)