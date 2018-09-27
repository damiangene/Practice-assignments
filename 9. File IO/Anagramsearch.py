lines = []
words = []
word_dict = {}
users_wdict = {}

def word_to_dict(word):
    temp = {}
    for letter in word:       
        temp[letter] = temp.get(letter,0) + 1
    return temp

print ("****Anagram Finder****")
users_word = (input("Enter a word: ")).lower()
users_wdict[users_word] = word_to_dict(users_word)

words = [x.strip() for x in open("EnglishWords.txt", "r").readlines()]
words = words[words.index("START"):]

a = []
for word in words:
    word_dict[word] = word_to_dict(word) 
 
    if word == users_word:
        pass
    
    elif word_dict[word] == users_wdict[users_word]:
        a.append(word)

if len(a) > 0:
    print ("{}".format(a))

else:
    print ("Sorry, anagrams of {} could not be found.".format(users_word))