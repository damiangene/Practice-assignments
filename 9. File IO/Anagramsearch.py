lines = []
words = []
word_dict = {}
users_wdict = {}
a = []

print ("****Anagram Finder****")
users_word = input("Enter a word: ")
temp = {}
for letter in users_word:       
    if letter in temp:
        occ = temp.get(letter)
        occ += 1
    
    else:
        occ = 1
    
    temp[letter] = occ
users_wdict[users_word] = temp

with open("EnglishWords.txt", "r") as tmp_file:
    for line in tmp_file:
        lines.append(line.rstrip('\n'))

for element in lines:
    words.append(element)

words = words[words.index("START"):]
 
for word in words:
    temp = {}
    for letter in word:       
        if letter in temp:
            occ = temp.get(letter)
            occ += 1
        
        else:
            occ = 1
        
        temp[letter] = occ
    word_dict[word] = temp 
 
    if word == users_word:
        pass
    
    elif word_dict[word] == users_wdict[users_word]:
        a.append(word)

if len(a) > 0:
    print ("{}".format(a))

else:
    print ("Sorry, anagrams of {} could not be found.".format(users_word))