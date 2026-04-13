#calcullate n natural numbers

nums=6

def natural_numbers(nums):
    if(nums==0):
        return 0
    
    return natural_numbers(nums-1)+nums

number=natural_numbers(nums)
print(number)