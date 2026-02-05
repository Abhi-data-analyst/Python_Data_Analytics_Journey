def trend_analysis(data):
    valid=[]
    for x in data:
        if x>0:
            valid.append(x)
    trend_timeline=[]
    Up_streak=0
    down_streak=0
    same_streak=0
    max_UP=0
    max_down=0
    max_same=0
    for i in range(1,len(valid)):
        curr= valid[i]
        prev=valid[i-1]
        if prev<curr:
            Up_streak+=1
            down_streak=0
            same_streak=0
            trend_timeline.append("UP")
            max_UP=max(max_UP,Up_streak)
        elif prev==curr:
            same_streak+=1
            Up_streak=0
            down_streak=0
            trend_timeline.append("Same")
            max_same=max(max_same,same_streak)
        else:
            down_streak+=1
            Up_streak=0
            same_streak=0
            trend_timeline.append("Down")
            max_down=max(max_down,down_streak)
    return{"valid values":valid,
           "Trend timeline":trend_timeline,
           "Longest up streak":max_UP,
           "Longest same streak":max_same,
           "Longest down streak":max_down}

data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95,100,101,102,103]
result=trend_analysis(data)
for k, v in result.items():
    print(f"{k}:{v}")
