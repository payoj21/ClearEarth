#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup, Comment, Tag, NavigableString
from nltk.tokenize import sent_tokenize, word_tokenize
class Entity:
	def __init__(self, id, string, attr_dict, type):
		self.id = id
		self.string = string
		self.attr_dict = attr_dict
		self.type = type

class Token:
	label = 'O'
	def __init__(self, string, start, end):
		self.string = string
		self.start = start
		self.end = end

	def __repr__(self):
		return '{' + self.string + ', ' + str(self.start) + ', ' + str(self.end) + ',' + self.label + '}'

def conv2train(filename, path):
	# args = sys.argv
	# if len(args) < 2:
	# 	print('Specify input XML file.')
	# 	sys.exit()
	# print(args[0], args[1])
	# xml = args[1]

	arr = path.split('/');
	# print(arr)
	path_to_text = arr[0]+'/'+arr[1]+'/txt/'
	# print(path_to_text)
	path_to_train = arr[0]+'/'+arr[1]+'/train/'
	# print(path_to_train)
	print('Running for '+filename)
	txtfile = open(path_to_text+filename[:filename.find('.')] + '.txt', 'r', encoding = 'utf-8').read()
	output = open(path_to_train+filename[:filename.find('.')] + '.train', 'w')


	tokens = list()
	filetokens = word_tokenize(txtfile)

	ongoing_index = 0
	for tok in filetokens:
		index = txtfile.find(tok, ongoing_index)
		if index == -1:
			break
		tokens.append(Token(tok, index, index + len(tok)))
		ongoing_index = index

	xml = open(path+filename[:filename.find('.')] + '.xml', 'r')
	xmltxt = xml.read()
	print(xmltxt)
	xml.close()
	soup = BeautifulSoup(xmltxt)
	print(soup.findAll('entity'))
	for concept in soup.findAll('entity'):
		id = concept.id.get_text()
		type = concept.type.get_text()
		print(concept.span)
		spans = concept.span.get_text().split(';')
		string = ''
		# TODO how to handle disjoint spans?
		x, y = spans[0].split(',')
		x = int(x)
		y = int(y)
		string = txtfile[int(x):int(y)]
		print(txtfile)
		print (string)
		string = string.lower().rstrip('\'\"-,.:;!?')
		string = string.strip()

		for tok in tokens:
			# print('Beginning of the entity')
			if tok.start == x:

				tok.label = type + '-B' # conll does some shenanigans with only using B if next to another?
				if tok.end == y: # It's just this one token
					break
				else:
					continue
			if tok.start >= x and tok.end == y: # It's just this one token
				tok.label = type + '-I'
				break
			if tok.start >= x and tok.end < y: # keep looking
				tok.label = type + '-I'
				continue
			if tok.start >= x and tok.end > y: # this shouldn't happen
				tok.label = type + '-I'
				break

	output.write('-DOCSTART- -X- O O\n\n')
	for tok in tokens:
		if tok == '\n' or tok == ' ':
			continue
		output.write(tok.string + ' X X ' + tok.label + '\n')
		if tok.string in '.!?': # crap, what about quotes?
			output.write('\n')
