def readFile(file_name):
    words = []
    with open(file_name) as f:
        for line in f:
            words.append(line.rstrip().lower())
    return words

def countPalindromes(words):
    n = 0
    for w in words:
        print(f'Is \'{w}\' palindrome?')
        pal = ""
        for l in w:
            pal = l + pal
        print("Reversed: ",pal)
        if pal==w:
            n += 1
            print("YES!")
        else:
            print("NO!")
        print("----------------------------------")
    return n


fileName = "palindromes.txt"

try:
    words = readFile(fileName)
except FileNotFoundError as file_err:
    print(f'Error with \'{fileName}\' file! More info: ', file_err)
except:
    print(f'Undefined error!')
else:
    words = readFile(fileName)
    print("Words from txt file: ",words)
    print("Number of palindromes: ", countPalindromes(words))