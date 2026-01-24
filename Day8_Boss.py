def valid_data(marks):
    valid_count=0
    valid_sum=0
    valid_avg=0
    for x in marks:
        if x<=0:
            continue
        else:
            valid_count+=1
            valid_sum+=x
    valid_avg=valid_sum/valid_count
    return valid_avg
marks=[45,45,65,-1,-9,0,69,0,0,15]
print(valid_data(marks))