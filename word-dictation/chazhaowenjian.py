#coding:UTF-8
import os

def findfile(key,inputdir = "."):
	foundlist = []
	for roots, dirs, files in os.walk(inputdir):
		print "searching",roots,"..."
		# print dirs
		for file in files:
			full_name = roots + "/" + file
			if key in file:
				foundlist.append(full_name)
			with open(full_name) as f:
				for l in f.readlines():
					if key in l:
						foundlist.append(full_name + ":" + l)
	return foundlist
keyword = raw_input("keyword:")
roots = raw_input("in:")
if not roots.strip():
	roots = "."

result = findfile(keyword,roots)
print "\n=========== result ============\n\n"
for r in result:
	print r

		# onefile = open(roots + "\\" + file, "r")
		# content = onefile.read()
		# if keyword in content:
		# 	print(roots + "\\" + file)
