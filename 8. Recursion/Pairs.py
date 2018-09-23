def keep_count(sentence):
    def pairs(sentence, count):
        if len(sentence) == 1:
            return count           

        elif sentence[0] == sentence[1]:
            count += 1
            if len(sentence) == 2:
                return count
            else:
                sentence = sentence[2:len(sentence)]
                return pairs(sentence,count)
                
        else:
            sentence = sentence[1:len(sentence)]
            return pairs(sentence,count)
 
    print ("The sentence has {} pairs".format(pairs(sentence,count=0)))

sentence = ((input("What is your sentence?")).lower())
sentence = [a for a in sentence]
keep_count(sentence)

