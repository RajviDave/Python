#for plus mode

file1=open("demo.txt","r+")#this is reading and write mode
data=file1.read()
print(data)
file1.close()

file2=open("demo.txt","r+")
file2.write("1234")
file2.close()

file3=open("demo.txt","r+")
file3.write("first option")
file3.close()

file4=open("demo.txt",'r+')# the mode will start it's point from first position and over write existing characters
file4.write("prize")
file4.close()
