def streak_analysis(data):
    valid=[]
    for x in data:
        if x>0:
            valid.append(x)
    current_streak=1
    streak=[]
    for i in range(1,len(valid)):
        perv=valid[i-1]
        curr=valid[i]
        if perv<curr:
            current_streak+=1
        else:
            if current_streak>=3:
                streak.append(current_streak)
            current_streak=1
    if current_streak>=3:
            streak.append(current_streak)
    return{"Valid streak":valid,
           "Number of streaks":len(streak),
           "List of streak":streak}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=streak_analysis(data)
for k, v in result.items():
    print(f"{k}:{v}")
