def trend_analysis(fluctuation_data):
    total=0
    count=0
    for x in fluctuation_data:
        if x==0:
            continue
        if  x%2==0:
            count+=1
            total+=x
        else:
            continue
    avg=total/count
    return count, total, avg

fluctuation_data = [
    12, 5, 18, 0,15, 3, 
    20, 7, 14, 2, 0, 
    11, 20,8, 5, 9, 1
]
print(trend_analysis(fluctuation_data))