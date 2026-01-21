valid_marks=0
abscent=0
highest=0
lowest=99999
avg_marks=0
total_marks=0
marks = [90, 45, -1, 0, 76, 88, -1, 34, 100]
for x in marks:
    if x==-1:
        continue
    if x>0:
        valid_marks +=1
        total_marks+=x
    if x==0:
        abscent+=1
    if x>highest:
        highest=x
    if x<lowest and x!=0:
        lowest=x
average_marks=total_marks/valid_marks
print("Number of valid marks :-",valid_marks)
print("Number of abscent students:-",abscent)
print("Average marks of the class:-",average_marks)
print("Lowest marks in the class:-",lowest)
print("Highest marks in the class :-",highest)
