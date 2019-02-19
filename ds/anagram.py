# heart and earth are anagrams
# assumption, strings are of the same size
# they are made of the 24 alaphabets

def anagramSolution(s1, s2):
	alist = list(s2)

	pos1 = 0
	stillOk = True

	while pos1 < len(s1) and stillOk:
		pos2 = 0
		found = False

		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2 +1
			pass

		if found:
			alist[pos2] = None
		else:
			stillOk = False
			pass

		pos1 = pos1 +1
		pass

	return stillOk


print(anagramSolution('abcd', 'dcba'))
print(anagramSolution('earth', 'heart'))
print(anagramSolution('james', 'esjam'))