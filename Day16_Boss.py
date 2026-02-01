def full_trend_analysis(data):
    total_valid_days=0
    total_idle_data=0
    sum_of_valid_days=0
    low=0
    high=0
    same=0
    trend_timeline=[]
    up_streak=0
    down_streak=0
    same_streak=0
    valid=[]
    for x in data:
        if x==-1:
            continue
        elif x==0:
            total_idle_data+=1
            continue
        else:
            total_valid_days+=1
            sum_of_valid_days+=x
            valid.append(x)
    avg=sum_of_valid_days/total_valid_days
    for i in range (1, len(valid)):
        prev= valid[i-1]
        curr=valid[i]
        if prev<curr:
            high+=1
            low=0
            same=0
            up_streak= max(up_streak,high)
            trend_timeline.append("High")
        elif prev==curr:
            same+=1
            high=0
            low=0
            same_streak=max(same_streak,same)
            trend_timeline.append("Same")
        else:
            low+=1
            high=0
            same=0
            down_streak=max(down_streak,low)
            trend_timeline.append("Low")
    return{"Number of valid days":total_valid_days,
           "Number of idle days":total_idle_data,
           "Sum of valid days":sum_of_valid_days,
           "Number of Up streak":high,
           "Number of low streak":low,
           "Number of same streak":same,
           "List of trend analysis":trend_timeline}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=full_trend_analysis(data)
for key, value in result.items():
    print(f"{key}:{value}")
