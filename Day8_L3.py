def avg(data):
    sum=0
    valid_value=0
    for x in data:
        if x<=0:
            continue
        else:
            valid_value+=1
            sum+=x
    avg=sum/valid_value        
    return avg
data = [-45,55,87,0,-1,-1,-3,10, -1, 0, 25, -1, 40]
print(avg(data))
