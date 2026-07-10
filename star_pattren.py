# To print Star Pattren in Square 

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end = " ")
    print()


# To print Star pattren in triangle 

for i in range(1, 6):
    print("*" * i)


# To print Pyramid 

n = 5 

for i in range(1, n + 1):
    print(" " * (n - i) + " * " * i)
