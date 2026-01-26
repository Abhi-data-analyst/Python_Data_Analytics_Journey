def valid_data(data):
    highest=None
    for x in data:
        if x<=0:
            continue
        if x>highest:
            highest=x
    return highest
sales = [1200, 0, -1, 4500, 3200, -99, 0, 2100]
print(valid_data(sales))

