def get_quadruple(word):
    n = len(word)
    s = word
    new_word = ''.join([s[x+2:x+4]+s[x:x+2] for x in range(0, len(s), 2))
    print(new_word)
    return new_word 


def main():
    result = get_quadruple('Abcdefgh')
    if result == "cdabghef ":
        print("COrrect!")
main()
