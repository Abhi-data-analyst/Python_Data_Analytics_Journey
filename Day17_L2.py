def useful_insights(data):
    valid=[]
    total_valid_days=0
    count_up=0
    count_down=0
    count_same=0
    lsit_of_trends=[]
    for x in data:
        if x<=0:
            continue
        else:
            total_valid_days+=1
            valid.append(x)
    for i in range(1,len(valid)-1):
        prev= valid[i-1]
        curr=valid[i]
        if prev<curr:
            count_up+=1
            lsit_of_trends.append("UP")
        elif prev>curr:
            count_down+=1
            lsit_of_trends.append("DOWN")
        else:
            count_same+=1
            lsit_of_trends.append("SAME")
    return{"Nuber of valid days":total_valid_days,
           "Number of Up trends":count_up,
           "Number of Down trends":count_down,
           "Number of Same trends":count_same,
           "List of trends":lsit_of_trends}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=useful_insights(data)
for key, values in result.items():
    print(f"{key}:{values}")

