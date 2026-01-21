valid_data=0
valid_data_list=[]
missing_data=0
missing_data_list=[]
data = [25, -1, 0, 40, -3, 15, 0, -1, 60]
for x in data:
    if x==-1:
        continue
    if x>0:
        valid_data+=1
        valid_data_list.append(x)
    if x==0:
        missing_data+=1
        missing_data_list.append(x)
print("List of valid data:-",valid_data_list)      
print("List of missing data:-",missing_data_list)
print("Count of valid data:-",valid_data)
print("Count of missing data",missing_data)