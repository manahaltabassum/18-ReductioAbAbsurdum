book = []

with open("book.txt","r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        book += words
    #print book

def wordFreq(word):
    return len(list(filter(lambda x: x == word, book)))
    #print "The frequency of the word '" + word + "' is: " + str(wordOccurence)
    
def phraseFreq(phrase):
    phraseLen = len(phrase.split())
    groups = [book[i:i+phraseLen] for i in range(0, len(book)-phraseLen)]
    phraseOccurence = len([x for x in groups if x == phrase.split()])
    print "The frequency of the phrase '" + phrase + "' is: " + str(phraseOccurence)

#for each unique word in book, count the frequency of the word
wordFreqs = {word:wordFreq(word) for word in set(book)}

def mostFreq():
	return reduce(lambda a,b: a if wordFreqs[a] > wordFreqs[b] else b, wordFreqs)

print "frequency of the word 'the': "+ str(wordFreq("the"))
print "frequency of the word 'Hart': "+ str(wordFreq("Hart"))
phraseFreq("a loose network of")
phraseFreq("of the")

print "the most frequent word is " + "'"+ mostFreq() +"'"