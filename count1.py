import string

s = "The new patients were an 18-year-old female student who returned from Britain on Friday, and a 61-year-old man whose granddaughter and domestic helper was infected previously, according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s communicable disease branch."

def countLetter(word):
    
    count = {}
    result = []

    for character in word:
        character = character.lower()
        if (character in string.ascii_letters):
            count.setdefault(character,0)
            count[character] += 1

    for key, value in count.items():
        temp = [key, value]
        result.append(temp)
    result.sort()
    return result

print(countLetter(s))