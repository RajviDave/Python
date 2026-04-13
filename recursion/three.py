#print all elements of list
list=[1,2,3,4,5]

def print_elements(list,index):

    if(index==len(list)):
        return
    
    print(list[index])
    print_elements(list,index+1)

print_elements(list,0)