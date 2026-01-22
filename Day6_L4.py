valid_vlaue=[]
invalid_vlaue=[]
missing_vlaue=[]
data = [12, 0, -1, 45, -8, 0, 7, 90, 0, -1]
for x in data:
    if x>0:
        valid_vlaue.append(x)
    if x<0:
        invalid_vlaue.append(x)
    if x==0:
        missing_vlaue.append(x)
print("List of all valid vlaues:->",valid_vlaue)
print("List of all invalid vlaues:->",invalid_vlaue)
print("List of all missing values:->",missing_vlaue)       
