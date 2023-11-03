word = input("Enter a string: ")
if (word[-3:] == 'ing'):
    print(f"New String : {word[:-3]+'ly'}")
else:
    print(f"New String : {word+'ing'}")
