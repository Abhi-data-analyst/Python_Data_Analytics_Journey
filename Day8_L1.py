def valid_count(num):
    valid_value=0
    for x in num:
        if x==-1:
            continue
        elif x>0:
            valid_value+=1
    return valid_value
num = [10, -1, 0, 25, -1, 40]
print(valid_count(num))
