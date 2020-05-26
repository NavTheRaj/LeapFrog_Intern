import math
def logic(num):
    number = str(num)
    total = 0
    for i in range(len(number)):
        if i==0:
            n = int(number[i])
            power = int(number[-1])
        else:
            n = int(number[i])
            power = int(number[i-1])
        total = total+pow(n,power)
    return total
def main():
    num = 145
    result = logic(num)
    if result == 630:
        print("Correct")

main()
