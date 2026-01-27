def temprature(temp_data):
    cold_days=0
    normal_days=0
    total=0
    for x in temp_data:
        if x ==-99:
            continue
        if x<0:
            cold_days+=1
        else:
            normal_days+=1
            total+=x
    avg=total/normal_days
    return cold_days,normal_days,avg
temp_data = [
    85, -99, 42, 0, -1, 99, 100, -99, 7, 12, 
    -1, 0, 55, 68, -99, -99, 88, 92, 0, -1
]
print(temprature(temp_data))