def analyze_metrics(daily_metrics):
    total_valid_days=0
    total_load=0
    idle_days_count=0
    count_of_critical=0
    count_of_high=0
    count_of_normal=0
    count_of_low=0
    list_of_Critical_load_days=[]
    list_of_above_average_load_days=[]
    for x in daily_metrics:
        if x>0:
            total_valid_days+=1
            total_load+=x
        if x ==0:
            idle_days_count+=1
        if x >=90:
            list_of_Critical_load_days.append(x)
            count_of_critical+=1
        if 60<x<89:
            count_of_high+=1
        if 30<x<59:
            count_of_normal+=1
        if 1<x<29:
            count_of_low+=1
    average_load_of_valid_days=total_load/total_valid_days
    for x in daily_metrics:
        if x>average_load_of_valid_days:
            list_of_above_average_load_days.append(x)
    return{"Number of valid days":total_valid_days,
           "Sum of load on valid days":total_load,
           "Number of Idle days":idle_days_count,
           "Number of critical days":count_of_critical,
           "Number of high load days":count_of_high,
           "Number of Normal load days":count_of_normal,
           "Number of Low load days":count_of_low,
           "New list of critical load days":list_of_Critical_load_days,
           "New list of above average load days":list_of_above_average_load_days}
daily_metrics = [
    -1, 0, 25, 40, 75, 95,
    60, 30, 10, -1, 0, 88,
    92, 55, 20, 100
]
result=analyze_metrics(daily_metrics)
for key, value in result.items():
    print(f"{key}:{value}")


        

    
