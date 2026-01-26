def count_valid(data):
    valid_data=0
    for x in data:
        if x<=0:
            continue
        else:
            valid_data+=1
    return valid_data
quarterly_data = [
    45, 52, 0, 12, -1, 88, 92, 34, 41, 0, 55, 62, -1, 105, 
    48, 50, 0, 15, 22, 98, 112, 39, 44, 0, 25, -1, 82, 95, 42, 51, 0]
print(count_valid(quarterly_data))