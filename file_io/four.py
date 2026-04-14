#w plus mode

file1=open("demo.txt","w+")
file=file1.read()#file will be truncated in w plus mode so null will be printed out
print(file)
file1.close()

file2=open("demo.txt","w+t")
file2.write("Number seven stops")#it will create new file if does not exist and will truncate if exist
file2.close()