f=open("demo.txt",'r')
data=f.read()
print(data)
b=f.read(10)#it will only read 5 characters
print(b)
f.close()

a=open("demo.txt","r")
abc=a.readline(1)
print(abc)