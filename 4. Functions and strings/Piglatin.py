def to_english(sentence):
    s_list = (sentence.lower()).split()
    new_sentence = ""

    for word in s_list:
        original_word = ""
        if "way" in word:
            original_word = word[0:len(word)-3]
            
        elif "way" not in word:
            i = 1
            original_word = word[0:len(word)-2]
            for _ in word:
                if original_word[len(original_word)-i] == "a":
                    starting_letters = original_word[len(original_word)-(i-1):len(original_word)]
                
                else:
                    i += 1
            
            original_word = starting_letters + original_word[0:len(original_word)-(i)]
            
        new_sentence = new_sentence + original_word + " "

    print (new_sentence)



def to_pig_latin(sentence):
    s_list = (sentence.lower()).split()
    new_sentence = ""

    for word in s_list:
        new_word = ""
        if word[0] in "aeiou":
            new_word = word + "way"
        
        elif word[0] not in "aeiou":
            i = 0
            for letter in word:
                if letter not in "aeiou":
                    new_word += letter
                    i +=1
                
                elif letter in "aeiou":
                    break

            new_word = word[i:len(word)] + "a" + new_word + "ay"
        
        new_sentence = new_sentence + new_word + " "

    print (new_sentence)


def e_or_p():
    user_input = input("(E)nglish or (P)ig latin? \n")
    user_input = user_input.lower()

    if user_input == "e":
        sentence = input("What is your English sentence? \n")
        to_pig_latin(sentence)
    
    elif user_input == "p":
        sentence = input("What is your Pig Latin sentence? \n")
        to_english(sentence)

    else:
        e_or_p()

e_or_p()