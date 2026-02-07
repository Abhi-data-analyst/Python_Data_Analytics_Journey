def trend_analysis(data):
    valid=[]
    for x in data:
        if x>0:
            valid.append(x)
    trend_list=[]
    number_of_trends=0
    up_trend=0
    down_trend=0
    for i in range(1,len(valid)):
        curr= valid[i]
        prev=valid[i-1]
        if prev<curr:
            up_trend+=1
            trend_list.append("Up")
        elif prev>curr:
            down_trend+=1
            trend_list.append("DOWN")
        else:
            continue
        if prev<curr or prev>curr:
            number_of_trends+=1
    return{"Valid list":valid,
           "trend List":trend_list,
           "Number of trends":number_of_trends}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=trend_analysis(data)
for k, v in result.items():
    print(f"{k}:{v}")