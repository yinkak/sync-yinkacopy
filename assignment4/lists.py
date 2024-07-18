import math

def mathfunction(x):
    y = math.sqrt(abs(x))
    z = 5 * (x ** 3)

    return y + z

list = []
i = 0
while i < 5:
    x = float(input("Enter a number: "))
    list.append(mathfunction(x))
    i += 1

reverseList = [list[::-1]]
print(reverseList)
