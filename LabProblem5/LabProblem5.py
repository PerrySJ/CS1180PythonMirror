n = int(input("What is the value of N?"))

while n <= 0:
        print("Error: n must be positive")
        n = int(input("What is the value of N?"))

for i in range (1, n+1, 1):
        print(f"{i}:", end="")
        for j in range (1, i+1, 1):
            if (i % j == 0):
                print(f" {j}", end="")

        print("")

        

                

