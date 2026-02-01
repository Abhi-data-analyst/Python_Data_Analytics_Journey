def analyze_trend(data):
    total_valid_days=0
    sum_of_valid_data=0
    idle_days=0
    stable_days=0
    spike_days=0
    list_of_stable_days=[]
    list_of_spike_days=[]
    for x in data:
        if x==-1:
            continue
        elif x==0:
            idle_days+=1
            continue
        else:
            total_valid_days+=1
            sum_of_valid_data+=x
    avg=sum_of_valid_data/total_valid_days
    for x in data:
        if x<=0:
            continue
        if (avg-10)<x<(avg+10):
            stable_days+=1
            list_of_stable_days.append(x)
        elif x>=(avg+20):
            spike_days+=1
            list_of_spike_days.append(x)
    return{"Number of valid days":total_valid_days,
           "Sum of valid days":sum_of_valid_data,
           "Number of idle days":idle_days,
           "Number of stable days":stable_days,
           "Number of spike days":spike_days,
           "List of all stable days":list_of_stable_days,
           "List of all spike days":list_of_spike_days,
           "Average of valid days":avg}
data = [
    45, 78, 0, 90, -1, 65, 88,
    0, 55, 100, 34, -1, 80,
    23, 75, 60, 95
]
result=analyze_trend(data)
for key, value in result.items():
    print(f"{key}:{value}")
