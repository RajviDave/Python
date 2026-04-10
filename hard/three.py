#Store words and their frequencies from this list:
#["apple", "banana", "apple", "orange", "banana", "apple"].

fruits=["apple", "banana", "apple", "orange", "banana", "apple"]
final_fruits={}
number=0

for fruit in fruits:
    
    number=fruits.count('apple')
    dict={fruit:number}
    print(dict)

print(final_fruits)
