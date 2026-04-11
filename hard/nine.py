#Find elements that appear only in one of the two collections:
#{1,2,3,4} and {3,4,5,6}.

set1={1,2,3,4}
set2={3,4,5,6}

common_element=set1.intersection(set2)
union_element=set1.union(set2)
final_answer=common_element-union_element

print(final_answer)
