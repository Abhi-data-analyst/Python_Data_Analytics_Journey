def full_insight_analyzer(data):
    valid=[]
    for x in data:
        if x<=0:
            continue
        else:
            valid.append(x)
    for i in range(1,len(valid)):
        prev=valid[i-1]
        curr=valid[i]
        current_up=0
        current_down=0
        current_same=0
        max_up_streak=0
        max_down_streak=0
        Max_same_streak=0
        full_trend_timeline_list=[]
        if prev<curr:
            current_up+=1
            current_same=0
            current_down=0
            max_up_streak=max(max_up_streak,current_up)
            full_trend_timeline_list.append("UP")
        elif prev==curr:
            current_same+=1
            current_down=0
            current_up=0
            Max_same_streak=max(Max_same_streak,current_same)
            full_trend_timeline_list.append("SAME")
        else:
            current_down+=1
            current_same=0
            current_up=0
            max_down_streak=(max_down_streak,current_down)
            full_trend_timeline_list.append("DOWN")
    max_sum=0
    best_window=[]
    for i in range(1,len(valid)-2):
        window_sum= valid[i]+valid[i+1]+valid[i+2]
        if window_sum>max_sum:
            max_sum=window_sum
            best_window=[valid[i],valid[i+1],valid[i+2]]
    return{"New list of only valid values":valid,
           "List of trend timeline":full_trend_timeline_list,
           "Longest UP streak":max_up_streak,
           "Longest Down streak":max_down_streak,
           "Longest Same streak":Max_same_streak,
           "Max 3 day sum":max_sum,
           "Best 3 day window":best_window
           }
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=full_insight_analyzer(data)
for key, value in result.items():
    print(f"{key}:{value}")
