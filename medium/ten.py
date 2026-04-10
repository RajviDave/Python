#Merge two mappings:
#{"a":1, "b":2} and {"c":3, "d":4}.

one={"a":1, "b":2}
two={"c":3, "d":4}

one.update(two)
print(one)