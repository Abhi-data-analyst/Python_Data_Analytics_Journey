def result(data):
    count=0
    sum_valid_data=0
    result=0
    for x in data:
        if x<=0:
            continue
        else:
            count+=1
            sum_valid_data+=x
    result=sum_valid_data/count
    return result
data1 = [-45,55,87,0,-1,-1,-3,10, -1, 0, 25, -1, 40]
inventory_stock = [15, -1, 0, 42, -1, 7, 100]
city_temps = [28, 30, -1, 25, 32, -1, 19]
app_ratings = [5, 4, 0, 2, -1, 5, 0, 3]
aisle_data = [500, 250, -1, 0, 1200, 750, -1]
delivery_logs = [120, 45, -1, 30, 0, 60, -1, 15]
print(result(data1))
print(result(inventory_stock))
print(result(city_temps))
print(result(app_ratings))
print(result(aisle_data))
print(result(delivery_logs))