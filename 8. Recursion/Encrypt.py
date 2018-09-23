def encrypt(sentence,count):
    if count >= len(sentence):
        exit()

    if ((sentence[count]).isalpha()) and ((sentence[count]) == (sentence[count]).lower()):
        sentence[count] = chr(97 + (ord(sentence[count]) + 1 - 97) % 26)
        print ("{}".format(sentence[count]), end = "")
        count += 1        
        return encrypt(sentence,count)

    else:
        sentence[count] = sentence[count]
        print ("{}".format(sentence[count]), end = "")
        count += 1        
        return encrypt(sentence,count)

        

sentence = (input("What is your sentence?"))
sentence = [a for a in sentence]
encrypt(sentence,0)