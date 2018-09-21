def bad_words():
    ignore = ((input("Enter words to be ignored (separated by commas): ")).lower()).split(", ")
    return ignore

def acronym():
    ignore = bad_words()
    print (ignore)
    acronym = ""
    title = ((input("Enter a title to generate its acronym: ")).lower()).split()
    for word in title:
        if word in ignore:
            pass
        else:
            acronym += (word[0]).title()+"."
    
    print (acronym)


acronym()
