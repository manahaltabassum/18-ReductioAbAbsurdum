book = []

with open("book.txt","r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        book += words
    #print book

def wordFreq(word):
    wordOccurence = len(list(filter(lambda x: x == word, book)))
    print "The frequency of the word '" + word + "' is: " + str(wordOccurence)
    
def phraseFreq(phrase):
    phraseLen = len(phrase.split())
    groups = [book[i:i+phraseLen] for i in range(0, len(book)-phraseLen)]
    phraseOccurence = len([x for x in groups if x == phrase.split()])
    print "The frequency of the phrase '" + phrase + "' is: " + str(phraseOccurence)

wordFreq("the")
wordFreq("Hart")
phraseFreq("a loose network of")
phraseFreq("of the")
