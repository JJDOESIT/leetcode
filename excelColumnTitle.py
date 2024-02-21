
def convertLetterToNumber(letter):
    return ord(letter) - 64

# Base 26 place values


def titleToNumber(columnTitle: str):
    total = 0
    count = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        total += convertLetterToNumber(columnTitle[i]) * (26**count)
        count += 1
    print(total)


titleToNumber("AB")
