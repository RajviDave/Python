#recursion

num=5
def recursion(num):
    if (num==0)|(num==1):
        return 1
    
    return recursion(num-1)*num

answer=recursion(num)
print(answer)