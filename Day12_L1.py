def data_value(extreme_data):
    valid=0
    invalid=0
    zero=0
    for x in extreme_data:
        if x <0:
            invalid+=1
        elif x==0:
            zero+=1
        else:
            valid+=1
    return invalid, valid, zero
extreme_data = [
    85, -99, 42, 0, -1, 99, 100, -99, 7, 12, 
    -1, 0, 55, 68, -99, -99, 88, 92, 0, -1
]

print (data_value (extreme_data))