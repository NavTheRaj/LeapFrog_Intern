def get_count(word):
    lower = word.lower()
    final = ""
    vowel_counts = {}
    for vowel in "aeiou":
        count = lower.count(vowel)
        vowel_counts[vowel]=count
    for key in vowel_counts:
        if vowel_counts[key]:
            result = ''.join(str(vowel_counts[key])+str(key))
            final = final+result
    if final: 
        return final
    else:
        pass


def main():
    result = get_count("qwtyp")
    print(result)
    if result == "3e1i2o":
        print("Correct")
main()
