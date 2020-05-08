sentence = []
word = []
sentence = input("enter a sentence\n")
sentence = sentence.split()

for i in sentence:
	if i not in word:
		word.append(i)

for i in range(0,len(word)):
	word.sort(key = str)
	print( word[i]," : ",sentence.count(word[i]))