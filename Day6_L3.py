highest=0
lowest=999
valid_marks=0
absentees=0
total=0
marks = [90, 0, -1, 45, 88, 76, 0, -1, 34, 100]
for x in marks:
    if x==0:
        continue
    if x==-1:
        absentees+=1
    if x>0:
        valid_marks+=1
        total+=x
        if x>highest:
            highest=x
        elif x<lowest:
            lowest=x
avg= total/valid_marks
print("Count of valid marks:->",valid_marks)
print("count of absentees:->",absentees)
print("Total valid marks :->",total)
print("Average of all valid marks :->",avg)
print("Highest valid marks :->",highest)
print("Lowest valid marks:->",lowest)
        


