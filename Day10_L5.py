def valid_data(data):
    pos_count=0
    neg_count=0
    for x in data:
        if x ==0:
            continue
        if x>0:
            pos_count+=1
        if x<0:
            neg_count+=1
    return pos_count,neg_count
data = [45, -12, 0, 89, -33, 0, 56, -102, 15]
print(valid_data(data))
