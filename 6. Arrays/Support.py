def welcome():
    print('Welcome to the automated techincal support system.')
    print('Please describe your problem')

def get_input():
    return input().lower()


def main():

    welcome()    
    query = get_input()   
    
    responses = {
                    "crashed": "Are the drivers up to date?", 
                    "blue": "Ah, the blue screen of death. And then what happened?", 
                    "hacked": "You should consider installing anti-virus software.", 
                    "bluetooth": "Have you tried mouthwash?",
                    "windows": "Ah, I think I see your problem. What version?",
                    "apple": "You do mean the computer kind of apple don't you?",
                    "spam": "You should see if your mail client can filter messages.",
                    "connection": "Contact Telkom."
                }
    
    while (not query=='quit'):
        query = query.split()
        
        for word in query:
            if word in responses:
                print(responses.get(word))
                break

            elif word == query[(len(query) - 1)]:
                print('Curious, tell me more.')                
            
        query = get_input()

if __name__ == "__main__":
    main()