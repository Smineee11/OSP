#!/usr/bin/python

import re

def ins(re1,re2):
	list1 = list(set(re1) & set(re2))
	ITS_List = sorted(list(map(int,list1)))
	return ITS_List


def uni(re1, re2):
	list2 = list(set(re1) | set(re2))
	UN_List = sorted(list(map(int,list2)))
	return UN_List


