import collections

while True:

    print("Enter a password:", end = ' ')
    password = str(input())
    if(password == "quit"):
        sys.exit(0)
    print("")
    print("Password validation")

    # checks length of password
    
    passwordLength = len(password)
    if passwordLength >= 9 and passwordLength <= 18:
        validLength = True
    else: 
        validLength = False

    # contains spaces
    
    if " " in password:
        validSpace = False
    else:
        validSpace = True

    # digit count param
    
    digitCount = 0
    for digit in password:
        if digit.isdigit():
            digitCount += 1

    if digitCount >= 2:
        validDigitCount = True
    else:
        validDigitCount = False

    # general letter count param
    letterCount = 0

    for letter in password:
        if(letter.isalpha()):
            letterCount += 1

    if letterCount >= 4:
        validLetterCount = True
    else:
        validLetterCount = False


    # vowel count param
    def isVowel(vowel):
        return vowel.upper() in ['A', 'E', 'I', 'O', 'U']
    
    vowelCount = 0
    for w in range(len(password)):

        # Check for vowel
        if isVowel(password[w]):
            vowelCount += 1

    if vowelCount >= 2:
        validVowelCount = True
    else:
        validVowelCount = False


    # upper case letter count parm
    upperLetterCount = 0

    for upper in password:
        if upper.isupper():
            upperLetterCount += 1

    if upperLetterCount >= 1:
        validUpperLetterCount = True
    else:
        validUpperLetterCount = False


    # lower case letter count param
    lowerLetterCount = 0

    for lower in password:
        if lower.islower():
            lowerLetterCount += 1           

    if lowerLetterCount >= 1:
        validLowLetterCount = True
    else:
        validLowLetterCount = False

    # special character count
    specialCount = 0
    for i in password:
        if i == '@':
            specialCount += 1
        elif i == '#':
            specialCount += 1
        elif i == '$':
            specialCount += 1
        elif i == '&':
            specialCount += 1
    if specialCount >= 2:
        validSpecialCount = True
    else:
        validSpecialCount = False


    # consecutive identical letters 

    # puts all of the characters into a list to check if there are multiple occurances of a specific character
    sameCount = 0
    sameLengthPassword = len(password) + 1
    for p in range(0,len(password)):
        if p == 0:
            continue
        if password[p] == password[p-sameLengthPassword]:
            sameCount += 1

    if sameCount >= 1:
        validChar = False
    else:
        validChar = True


    print("9 to 18 characters:", validLength)
    print("No spaces:", validSpace)
    print("At least 2 digits:", validDigitCount)
    print("At least 4 letters:", validLetterCount)
    print("At least 2 vowels:", validVowelCount)
    print("At least one uppercase letter:", validUpperLetterCount)
    print("At least one lowercase letter:", validLowLetterCount)
    print("At least two special characters from ['$','#','@','&']:", validSpecialCount)
    print("No two consecutive identical characters:", validChar)

    if validLength and validSpace and validDigitCount and validVowelCount and validLetterCount and validUpperLetterCount and validUpperLetterCount and validLowLetterCount and validChar:
        print("")
        print("Password " + password + " is valid!")
            # The output of the counters

        digitCount = 0
        for char in password:
            if char.isdigit():
                digitCount += 1

        print("Number of digits:", digitCount)

        vowelCount = 0
        for w in range(len(password)):
            if isVowel(password[w]):
                vowelCount += 1

        print("Number of vowels:", vowelCount)

        upperLetterCount = 0
        for upper in password:
            if upper.isupper():
                upperLetterCount += 1
        print("Number of uppercase letters:", upperLetterCount)

        lowerLetterCount = 0
        for lower in password:
            if lower.islower():
                lowerLetterCount += 1   

        print("Number of lowercase letters:", lowerLetterCount)

        specialCount = 0
        for k in password:
            if k == '@':
                specialCount += 1
            elif k == '#':
                specialCount += 1
            elif k == '$':
                specialCount += 1
            elif k == '&':
                specialCount += 1

        print("Number of special characters:", specialCount)
        break
    else:
        print("Password " + password + " is invalid. Try again.")
        print("")
        continue
    








    
    
        