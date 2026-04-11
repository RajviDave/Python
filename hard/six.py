#Remove all even numbers from [1,2,3,4,5,6,7,8].

data=[1,2,3,4,5,6,7,8]

for i in data:
    if i%2==0:
        data.remove(i)

print(data)