highest=0
lowest=99
valid_marks=0
total_marks=0
absentees=0
marks = [90, 0, -1, 45, 88, 76, 0, -1, 34]
for x in marks:
    if x==-1:
        continue
    if x>0:
        valid_marks+=1
        total_marks+=x
    if x>highest:
        highest=x
    if x<lowest and x>0:
        lowest=x
    if x==0:
        absentees+=1
avg_valid_marks=total_marks/valid_marks
print("Highest valid marks:->",highest)
print("lowest valid marks:->",lowest)
print("Number of absentees",absentees)
print("Average of all valid marks :->",avg_valid_marks)