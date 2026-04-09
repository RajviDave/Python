#does not have indexing 
#are mutable
#does not allow duplicate keys

students={'rajvi':38, 41:'dhruvi', 'priyanshi':43,'subjects': ['math','science','english'],'dict':{'sem':1,'next':3}}
#print(type(students))

print(students.keys()) #it will print all the keys of dictionary
print(students.values())#it will print all values
print(students.items())#it will print all key and value pairs
print(students.get('rajvi'))
print(students['rajvi'])
students.update({'umang':25})
print(students)

