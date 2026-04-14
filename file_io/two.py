#for write mode

file1=open("demo.txt","wt") #here wt mode will earase everything in file and write text
file1.write("I have javascript and typescript as their multiple report.")
file1.close()

file2=open("demo.txt","at")#here at mode will append text in the back of the existing text in the file
file2.write("12345")
file2.close()

file3=open("Sample.txt","wt")#here sample.txt does not exist but system will create it for us
file3.write("678")
file3.close()