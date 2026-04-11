#Given student marks
#{ "A":78, "B":92, "C":88, "D":67 }
#find the student with highest marks.

marks={ "A":78, "B":92, "C":88, "D":67 }

highest_mark=0

for mark in marks.values():
    if mark>highest_mark:
        highest_mark=mark

print("Highest mark is =")
print(highest_mark)