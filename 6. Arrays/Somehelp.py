import random

def welcome():
    print('Welcome to the automated techincal support system.')
    print('Please describe your problem')

def get_input():
    return input().lower()


def main():

    welcome()    
    query = get_input()   
    
    responses = {
                    1: "Have you tried it on a different operating system?", 2: "Did you reboot it?", 
                    3: "What colour is it?", 4: "You should consider installing anti-virus software.",
                    5: "Contact Telkom.", 6: "I'd get that looked at if I were you."
                }
    
    while (not query=='quit'):
        response_choice = random.randint(1,6)
        
        print(responses.get(response_choice))

        query = get_input()
    
if __name__ == "__main__":
    main()