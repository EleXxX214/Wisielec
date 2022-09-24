import sys


from re import A


letters = []
used_letters = []
life = 5



def find_indexes(word,guessing_letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if guessing_letter == letter_in_word:
                indexes.append(index)
    return indexes



word = input("Podaj słowo do wisielca:")

for _ in word:
    letters.append("_")


while life >= 1:
 
    print("----------------")
    print("Pozostało żyć:",life)
    print("----------------")
    print(letters)
    print("\n")

    while True:
        guessing_letter = input("Podaj litere:")
        
        if len(guessing_letter) == 1 and guessing_letter.isdigit() is False and guessing_letter.isalpha() is True:
            break
        
        
    print(type(guessing_letter))


    print("\n")

    if guessing_letter in used_letters:
        life -= 1
    used_letters.append(guessing_letter)

    found_indexes = find_indexes(word,guessing_letter)

    if len(found_indexes) == 0:
        print("!!!!!!!!!!!!!!!!!!!!")
        print("Nie ma takiej litery")
        print("!!!!!!!!!!!!!!!!!!!!")
        life = life - 1
        if life == 0:
            sys.exit(0)
    else:
        for index in found_indexes:
            letters[index] = guessing_letter
    if "".join(letters) == word:
        print("Brawo wygrałes !")
        sys.exit(0)    

    print("\n")
    print("Użyte litery:",used_letters)
    





    



    





 