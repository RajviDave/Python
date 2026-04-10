#From [5, 10, 15, 20, 25, 30], create a new collection containing only numbers divisible by 10.

nums=[5, 10, 15, 20, 25, 30]
new_nums=[]
for i in nums:
    if i%10==0:
        new_nums.append(i)

print(new_nums)
