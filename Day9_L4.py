def output(data):
    count = 0
    total = 0

    for x in data:
        if x == -1:
            continue
        count += 1
        total += x

    if count == 0:
        return (0, 0, 0)

    avg = total / count
    return (count, total, avg)
student_marks = [85, 92, -1, 78, 0, 95, 88, -1, 72, 100]
daily_sales = [1200, 0, 450, 700, -1, 1500, 2100, 0, -1, 950]
weather_readings = [22, 25, -1, 28, 24, -99, 21, 26, 23, -1]
print(output(student_marks))
print(output(daily_sales))
print(output(weather_readings))