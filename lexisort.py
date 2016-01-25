
# O ( n*m (log n*m) )
# m is length of string element

def lexicographicsort(args):
	listToSort, lexP = args	
	global lexParam, cache
	cache = dict()
	lexParam = buildMap(lexP) 
	return _mergesort(listToSort)

def _mergesort(listToSort):
	aSize = len(listToSort)
	if aSize == 1:
		return listToSort
	elif aSize > 1:
		middle = aSize/2
		aList = listToSort[:middle]
		bList = listToSort[middle:]
		return merge(_mergesort(aList), _mergesort(bList))

def merge(aList,bList):
	tmp = list()

	while aList and bList:
		if (lexisort(aList[0],bList[0])): 
			tmp.append(aList.pop(0))
		else:
			tmp.append(bList.pop(0))

	if aList:
		tmp.extend(aList)

	if bList:
		tmp.extend(bList)

	return tmp

def lexisort(a,b):
	return getMap(a, lexParam) < getMap(b, lexParam)

def buildMap(lexParam):
	return dict([(a,k) for a,k in zip(lexParam,range(len(lexParam)))] )

def getMap(s, lexParam):
	if s in cache:
		return cache[s]
	else:
		cache[s] = ''.join(str(lexParam[a]) for a in s)
		return cache[s]

if __name__ == "__main__":
	data = [ (["acb", "abc", "bca"], "abc"),
			 (["acb", "abc", "bca"], "cba"), 
			 (["aaa", "aa", ""], "a") ];

	for d in data:
		print d, '=>', lexicographicsort(d)
