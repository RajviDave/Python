#Find elements that appear only in one of the two collections:
#{1,2,3,4} and {3,4,5,6}.

set1={1,2,3,4}
set2={3,4,5,6}

result = set1.symmetric_difference(set2)

print(result)