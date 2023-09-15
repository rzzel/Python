secret_word = "chupacabra"
print("You are in a loop.")
while True:
    word = input("Enter a word: ")
    if word == secret_word:
        print("You've successfully left the loop.")
        break
        
        
    else:
        print("Wrong")