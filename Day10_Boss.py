def valid_data(data):
    count=0
    total=0
    for x in data:
        if x <=0:
            continue
        else:
            count+=1
            total+=x
    avg=total/count
    return count,total,avg
region_north = [1200, 1500, -1, 0, 2200, 1800, -1, 3000, 2500, 0]
sensor_readings = [22, 23, 21, -99, 24, 25, -1, 22, 21, 23]
daily_visitors = [450, 0, 0, 0, 520, 610, 0, 0, 800, 950]
app_stars = [5, 4, 1, 2, -1, 5, 0, 3, 4, 5]
warehouse_stock = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
print(valid_data(region_north))
print(valid_data(sensor_readings))
print(valid_data(daily_visitors))
print(valid_data(app_stars))
print(valid_data(warehouse_stock))