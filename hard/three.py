#Store words and their frequencies from this list:
#["apple", "banana", "apple", "orange", "banana", "apple"].

fruits=["apple", "banana", "apple", "orange", "banana", "apple"]
final_fruits={}

for fruit in fruits:
    if fruit not in final_fruits:
        final_fruits[fruit]=fruits.count(fruit)
    
print(final_fruits)
