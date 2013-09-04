#Amaka Atoyebi
#10.7
def is_anagram(an1, an2):
	sep1 = list(an1)
	sep2 = list(an2)
	if (len(sep1) == len(sep2)):
		for i in range(len(sep2)):
			if sep1[i] in sep2:
				return True
	return False	
		
		
is_anagram('strong', 'trongs')	

#10.13
readFile = open('words.txt')
line = readFile.readline()
wordList = []
for line in readFile:
	wordList.append(line.strip())

def does_interlock(s):
	sep1 = s[1::2]
	sep2 = s[::2]
	if (sep1 in wordList) and (sep2 in wordList):
		print sep1 + ", " + sep2

does_interlock('schooled')	

