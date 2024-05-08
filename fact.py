def fact(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n -1
    print(fact)
    
fact(3)