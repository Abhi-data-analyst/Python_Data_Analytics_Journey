def valid_values(units_sold):
    count=0
    for x in units_sold:
        if x ==-1:
            continue
        else:
            count+=1
    return count
units_sold = [45, 12, -1, 0, 89, 33, -1, 56, 102, 0]
print(valid_values(units_sold))