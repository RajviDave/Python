#a plus mode
file1=open("demo.txt","a+") #pointer at the end, so does not print anything
data=file1.read()
print(data)
file1.close()

file2=open("demo.txt","a+")
file2.write("My name is rajvi")#this text will be appened at the end of existing text
file2.close()