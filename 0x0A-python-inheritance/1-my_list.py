#!/usr/bin/python3
class MyList(list):
	def print_sorted(self):
		a = []
		for i in sorted(self):
			a.append(i)
		print(a)
