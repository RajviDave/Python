#Flatten this structure into a single sequence:
#[(1,2), (3,4), (5,6)].

nums=[(1,2), (3,4), (5,6)]

result=[]
for tup in nums:
    for data in tup:
        result.append(data)

print(result)