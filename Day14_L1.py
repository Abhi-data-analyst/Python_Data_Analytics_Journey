def real_data(sensor_readings):
    valid_reading_count=0
    sum_of_valid_reading=0
    list_of_valid_readings=[]
    for x in sensor_readings:
        if x<=0:
            continue
        else:
            valid_reading_count+=1
            sum_of_valid_reading+=x
            list_of_valid_readings.append(x)
    avg_valid_readings=sum_of_valid_reading/valid_reading_count
    return{"Number of valid readings":valid_reading_count, "Sum of valid readings":sum_of_valid_reading,"New corrected list":list_of_valid_readings,"Average of valid readings":avg_valid_readings}
sensor_readings = [
    -1, 0, 100, 45, -1, 0, 88, 12, -1, 99,
    0, 75, 1, 0, -1, 50, 66, -1, 0, 92
]
print(real_data(sensor_readings))