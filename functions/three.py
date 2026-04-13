#factorial

num=5

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

number=factorial(num)
print(number)
