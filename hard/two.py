#Find the second largest number in [12, 45, 23, 67, 34, 89, 54]
numbers=[100,99,98,97]

max1=max2=0
for i in numbers:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2:
        max2=i
    
print("second largerst is =")
print(max2)