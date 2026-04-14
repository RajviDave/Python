f=open("demo.txt","r") # if we do not mention mode here it will defalt consider 'r' read mode.
data=f.read(5)#read(n) will read first n characters and we do not mention 'n' then it will read whole text
print(data)
print(type(data))
f.close()

a=open("demo.txt",'r')
data=a.readline()#this will read file line by line
print(data)

line2=a.readline()
print(line2)#to read second line we will agaiin write readline() function

line3=a.readline()
print(line3)

a.close()