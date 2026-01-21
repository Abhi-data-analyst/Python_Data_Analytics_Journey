valid_value=0
invalid_value=0
missing_value=0
total_of_valid=0
data = [10, -1, 0, 25, -1, 40, 0, 60, 15]
for x in data:
    if x>0:
        valid_value+=1
        total_of_valid+=x
    elif x==0:
        missing_value+=1
    else:
        invalid_value+=1
print("Number of valid inputs :->",valid_value)
print("Number of invalid inputs:->",invalid_value)
print("Number of missing inputs:->",missing_value)
print("Total valid data:->",total_of_valid)


