num1 = 0
num2 = 1

n = int(input("What is the value of N? "))

while (n <= 0):
    print("Error: n cannot be negative or zero")
    n = int(input("What is the value of N? "))

print(1)
for i in range(n-1):
    nextNum = num1 + num2
    num1 = num2
    num2 = nextNum
    print(nextNum)


