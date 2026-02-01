def analyze_trend_direction(data):
    total_valid_days=0
    total_idle_days=0
    sum_of_valid_days=0
    up_trend=0
    down_trend=0
    same_trend=0
    list_of_trend_movement=[]
    valid=[]
    for x in data:
        if x==0:
            total_idle_days+=1
        if x > 0:
           total_valid_days += 1
           sum_of_valid_days += x
           valid.append(x)
    for i in range(1, len(valid)):
               prev = valid[i-1]
               curr = valid[i]
               if curr > prev:
                   up_trend += 1
                   list_of_trend_movement.append("UP")
               elif curr < prev:
                    down_trend += 1
                    list_of_trend_movement.append("DOWN")
               else:
                same_trend += 1
                list_of_trend_movement.append("SAME")
    return{"Number of valid days":total_valid_days,
           "Number of idle days":total_idle_days,
           "Sum of valid days":sum_of_valid_days,
           "Number of up trends":up_trend,
           "Number of down trends":down_trend,
           "Number of same trends":same_trend,
           "list of trends":list_of_trend_movement
           }
data = [
    45, 78, 78, -1, 65, 88,
    0, 55, 100, 34, -1, 80,
    80, 95
]
result=analyze_trend_direction(data)
for key, value in result.items():
    print(f"{key}:{value}")
