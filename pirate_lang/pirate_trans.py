import re

def get_trans(word):
    puncs = ".,;:?!"
    result =""
    final = ""
    new = re.findall(r"[\w']+|[.,!?;]", word)
    for i in range(len(new)):
        punc = re.findall(r"[.,!?;]", new[i])
        if punc:
            result = result.rstrip()+(new[i])+" "
        if not punc:
            result = result+new[i][1:]+new[i][0]+"arg"+" "
        
    return result.rstrip()
            

def main():
    result = get_trans("Take what you can,give nothing back.")
    print(result)
    if result == "akeTarg hatwarg ouyarg ancarg, ivegarg othingnarg ackbarg.":
        print("correct")
main()
