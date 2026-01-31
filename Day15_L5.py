def analyze_system_usage_refactored(server_data):
    total_valid_days=0
    total_idle_days=0
    sum_of_total_usage=0
    count_low=0
    count_high=0
    count_mid=0
    list_non_idle_valid_usage=[]
    list_of_high_usage_value=[]
    for day_list in server_data:
        for x in day_list:
            if x==-1:
                continue
            if x==0:
                total_idle_days+=1
                continue
            else:
                total_valid_days+=1
                sum_of_total_usage+=x
                list_non_idle_valid_usage.append(x)
            if 1<=x<=49:
                count_low+=1
            elif 50<=x<=79:
                count_mid+=1
            elif x>=80:
                count_high+=1
                list_of_high_usage_value.append(x)
    avg=sum_of_total_usage/total_valid_days
    return{"Number of valid days":total_valid_days,
           "Number of idle days":total_idle_days,
           "Total usage":sum_of_total_usage,
           "Number of low usage days":count_low,
           "Number of mid usage days":count_mid,
           "Number of high usage days":count_high,
           "List of non idle valid usage days":list_non_idle_valid_usage,
           "List of high usage values":list_of_high_usage_value,
           "Average of valid usage days":avg}
server_data = [
    [45, 78, 0, 90, -1, 65, 88],
    [0, 55, 100, 34, -1, 80],
    [23, 0, 75, 60, 95, -1]
]
result=analyze_system_usage_refactored(server_data)
for key, value in result.items():
    print(f"{key}:{value}")

