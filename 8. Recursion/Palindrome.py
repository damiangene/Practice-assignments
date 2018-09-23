sentence = ((input("Enter a string: ")).lower()).replace(" ","")

def palindrome(sentence):
    if len(sentence)  <= 2:
        if sentence[0] == sentence[len(sentence)-1]:
            print ("This is a palindrome")
        else:
            print ("This is not a palindrome")

    elif sentence[0] != sentence[len(sentence)-1]:
       print ("This is not a palindrome")
    
    else:
        sentence = sentence[1:len(sentence)-1]
        palindrome(sentence)

palindrome(sentence)