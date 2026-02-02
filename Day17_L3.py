def new_insights(data):
    current_up=0
    current_down=0
    current_same=0
    max_up=0
    max_down=0
    max_same=0
    valid=[]
    trend_timeline=[]
    for x in data:
        if x<=0:
            continue
        else:
            valid.append(x)
    for i in range (1,len(valid)-1):
        prev=valid[i-1]
        curr=valid[i]
        next=valid[i+1]
        if prev<curr:
            current_up+=1
            current_down=0
            current_same=0
            trend_timeline.append("UP")
            max_up=max(max_up,current_up)
        elif prev==curr:
            current_same+=1
            current_down=0
            current_up=0
            max_same=max(max_same,current_same)
            trend_timeline.append("SAME")
        else:
            current_down+=1
            current_same=0
            current_same=0
            max_down=max(max_down,current_down)
            trend_timeline.append("DOWN")
    return{"Longest UP streak":max_up,
           "Longest Down streak":max_down,
           "Longest Same streak":max_same,
           "List of trend analysis":trend_timeline}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=new_insights(data)
for key, value in result.items():
    print(f"{key}:{value}")