#Amaka Atoyebi
#11.9
readFile = open('words.txt')
line = readFile.readline()
word = line.strip	

#11.10
def rotate_word(string, integer):
	letters = string.split()
	new = ""
	for letters in string:
		if letters.isupper():
			start = ord('A') - 1
		elif letters.islower():
			start = ord('a') - 1
		else:
			return letters	
		letterToNum = ord(letters) - start
		moveFor = letterToNum + integer
		if moveFor > 26:
			moveFor = moveFor%26
		numToLetter = chr(moveFor)
		returnTo = moveFor + start
		newLetters = chr(returnTo)
		new += newLetters
	print new


def make_word_dict():
	d = dict()
	fin = open('words.txt')
	for line in fin:
		word = line.strip().lower()
		d[word] = word
	return d


def rotate_pairs(word, word_dict):
	for i in range(1, 14):
		rotated = rotate_word(word, i)
		if rotated in word_dict:
			print word, i, rotated


word_dict = make_word_dict()

for word in word_dict:
	rotate_pairs(word, word_dict)
   
