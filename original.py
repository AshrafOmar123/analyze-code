import math


def main():
    
    word = "Be Safe"
    
    for i in range(8):
        print(word[i])
    
    result = math.exp(2000)
    print(result)
    
    result2 = factorial(20000)
    print(result2)
    
def factorial(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)
    
    
main()
