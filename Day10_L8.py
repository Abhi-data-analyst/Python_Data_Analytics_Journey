def total_value(readings):
    valid_count=0
    total_count=0
    for x in readings:
        if x <=0:
            total_count+=1
        else:
            valid_count+=1
            total_count+=1
    percentage=valid_count/total_count*100
    return valid_count,total_count,percentage
readings = [22, 0, 25, -1, 28, 30, 0, 26]
print(total_value(readings))