valid_value=0
missing_value=0
total=0
data = [10, -1, 0, 25, -1, 40, 0, 60, 15]
for x in data:
    if x==-1:
        continue
    if x>0:
        valid_value+=1
        total+=x
    if x==0:
        missing_value+=1
avg=total/valid_value
print("Number of valid value:->",valid_value)
print("Number of missing value:->",missing_value)
print("Average of valid values:->",avg)
print("Total of all valid values ",total)
