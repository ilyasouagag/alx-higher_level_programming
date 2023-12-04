#!/usr/bin/python3
"""Define a class mylist and function print sorted"""
class MyList(list):
	"""Mylist class inhereted list attributes"""
	def print_sorted(self):
		"""print sorted method"""
		a = []
		for i in sorted(self):
			a.append(i)
		print(a)
