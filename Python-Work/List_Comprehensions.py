#Used to create a new list based on another list
#Specifiying the length of each word that isn#'t the
#How to get the word length not using a list comprehension
#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#word_lengths = []
#for word in words:
    #  if word != "the":
    #      word_lengths.append(len(word))
#print(words)
#print(word_lengths)

#How to achieve it using list comprehension
#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#word_lengths = [len(word) for word in words if word != "the"]
#print(words)
#print(word_lengths)