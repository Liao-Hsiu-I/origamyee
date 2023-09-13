def sumOfEvenDigits(s):
    res = 0
    for i in s:
        num = int(i)
        if(num % 2 == 0):
            res += num
    return res

s = "111652017"
print("sum of even digits =",sumOfEvenDigits(s))
