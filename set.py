#set is mutable but its values are immutable like mutable elements are not allowed(list and dictionary)
#we can not store duplicate values in set

rajvi={'1','2','3','4','4'} #even if you store duplicate value it will return only singular values
print(rajvi)

#methods in sets
rajvi.add('5')#it will add mentioned element
rajvi.remove('2')#remove mentioned element
rajvi.pop()#it will remove randomly any value
print(rajvi)
print(len(rajvi))#length of set
rajvi.clear()
print(rajvi)

#you can not store list and dictionary as it is mutable rest you can store anything
#set is unordered / not nessacery to print the way we have stored
#since set does nnot count duplicate values it will not consider in .count function as well
#immutable is hashable value like one value it will have fixed hashvalue and it will nto change for life time 
#immutable are hashable like tuple 
#mutable are unhashable like list, dictionary whose hashvalue can be changed also set is unhashable but its elements are not

set1={'1','2','3','4'}
set2={'5','6','7','8','4'}


print(set1.intersection(set2))#it will return us intersection of two sets
print(set1.union(set2))#it will return union of both sets

