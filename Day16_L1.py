def analyze_productivity(productivity_data):
    abscent=0
    total_valid_working_days=0
    total_productivity=0
    low_pro=0
    mid_pro=0
    high_pro=0
    list_above_avg_productivity_days=[]
    list_of_high_productivity_days=[]
    for x in productivity_data:
        if x==-1:
            continue
        elif x==0:
            abscent+=1
            continue
        else:
            total_valid_working_days+=1
            total_productivity+=x
        if 1<=x<=49:
            low_pro+=1
        elif 50<=x<=79:
            mid_pro+=1
        elif x>=80:
            high_pro+=1
            list_of_high_productivity_days.append(x)
    avg=total_productivity/total_valid_working_days
    for x in productivity_data:
        if x>avg:
            list_above_avg_productivity_days.append(x)
    return{"Number of abscent days":abscent,
           "NUmber of valid working days":total_valid_working_days,
           "Total productivity":total_productivity,
           "Number of day with low productivity":low_pro,
           "Number of days with Mid productivity":mid_pro,
           "Number of days with high productivity":high_pro,
           "List of days with above average productivity":list_above_avg_productivity_days,
           "list of days with high productivity":list_of_high_productivity_days}
productivity_data = [
    45, 78, 0, 90, -1, 65, 88,
    0, 55, 100, 34, -1, 80,
    23, 75, 60, 95
]
result=analyze_productivity(productivity_data)
for key, value in result.items():
    print(f"{key}:{value}")