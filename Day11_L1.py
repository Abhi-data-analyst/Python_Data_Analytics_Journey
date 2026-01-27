def value(sensor_data):
    valid_count=0
    invalid_count=0
    for x in sensor_data:
        if x ==-1:
            invalid_count+=1
            continue
        else:
            valid_count+=1

    return invalid_count, valid_count
sensor_data = [88, 92, -1, -1, 0, 45, -1, 102, 0, -1, 77, 81, -1, -1, 95]
print(value(sensor_data))