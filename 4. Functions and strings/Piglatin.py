def to_pig_latin(sentence):
    s_list = (sentence.lower()).split()
    s_list_new = []

    for word in s_list:
        new_word = ""
        if word[0] in "aeiou":
            new_word = word + "way"
            s_list_new.append(new_word) 
        
        elif word[0] not in "aeiou":
            i = 0
            for letter in word:
                if letter not in "aeiou":
                    new_word += letter
                    i +=1
                
                elif letter in "aeiou":
                    break

            new_word = word[i:len(word)] + "a" + new_word + "ay"
            s_list_new.append(new_word)       

    new_sentence = ""
            
    for word in s_list_new:
        if word == s_list_new[0]:
            new_sentence = ((word).title())
        
        else:
            new_sentence += " " + word

    print (new_sentence)



def to_english(sentence):
    s_list = (sentence.lower()).split()
    print (s_list)


def e_or_a():
    user_input = input("(E)nglish or (P)ig latin? \n")
    user_input = user_input.lower()

    if user_input == "e":
        sentence = input("What is your English sentence? \n")
        to_pig_latin(sentence)
    
    elif user_input == "a":
        sentence = input("What is your Pig Latin sentence? \n")
        to_english(sentence)

    else:
        e_or_a()

e_or_a()