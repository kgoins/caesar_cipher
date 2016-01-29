#!/usr/bin/python

from string import ascii_lowercase
from string import ascii_uppercase
from string import translate
from string import maketrans


def caesar(text, key):
	negative = False
	if key < 0:
		key = key * -1
		negative = True

	outLower = ascii_lowercase[key:] + ascii_lowercase[:key]
	outUpper = ascii_uppercase[key:] + ascii_uppercase[:key]

	inAlph = ascii_lowercase + ascii_uppercase
	outAlph = outLower + outUpper

	if negative: inAlph, outAlph = outAlph, inAlph

	transTable = maketrans(inAlph, outAlph)
	return text.translate(transTable)
