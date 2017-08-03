#coding:UTF8
import os

def findfile(key,inputdir = "."):
	foundlist= []
	for path, dirnames, filenames in os.walk(inputdir):
		# print "searhching",path, "..."
		for name in filenames:
			fullname = path + "/" + name
			if key in name:
				foundlist.append(fullname)
			with open(fullname) as f:
				for l in f.readlines():
					if key in l:
						foundlist.append(fullname + ":" + l)
	return foundlist

keyword = raw_input("search:")
path = raw_input("in:")
if not path.strip():
	path = "."

result = findfile(keyword,path)
print "\n==================result==================\n\n"
for r in result:
	print r