def analyze_system_usage(server_data):
    total_valid_days=0
    total_idle_days=0
    total_usage_sum=0
    count_of_low=0
    count_of_normal=0
    high_usage_days=0
    merged_list_of_all_high_usage_days=[]
    merged_list_of_all_non_idle_valid_days=[]
    for day_list in server_data:
        for x in day_list:
            if x ==-1:
                continue
            if x==0:
                total_idle_days+=1
            if x>0:
                total_valid_days+=1
                total_usage_sum+=x
                merged_list_of_all_non_idle_valid_days.append(x)
            if 1<=x<=49:
                count_of_low+=1
            if 50<=x<=79:
                count_of_normal+=1
            if x>=80:
                high_usage_days+=1
                merged_list_of_all_high_usage_days.append(x)
    average_usage=total_usage_sum/total_valid_days
    return{"Total number of valid days":total_valid_days,
           "Total number of idle days": total_idle_days,
           "Sum of total usage": total_usage_sum,
           "Number of low usage days":count_of_low,
           "Number of noramal usage days":count_of_normal,
           "Number of high usage days": high_usage_days,
           "New list of all high usage days":merged_list_of_all_high_usage_days,
           "New list of days except idle days":merged_list_of_all_non_idle_valid_days,
           "average":average_usage}
server_data = [
    [45, 78, 0, 90, -1, 65, 88],
    [0, 55, 100, 34, -1, 80],
    [23, 0, 75, 60, 95, -1]
]
result= analyze_system_usage(server_data)
for key, value in result.items():
    print(f"{key}:{value}")
