with open("demo.txt","r") as f:
    file=f.read()
    print(file)

with open("demo.txt","w") as f:
    f.write("Multiple Options")