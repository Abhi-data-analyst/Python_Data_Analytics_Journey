def analyze_values(data):
    valid=[]
    maximum_three_day_sum=0
    largest=0
    for x in data:
        if x ==-1:
            continue
        elif x==0:
            continue
        else:
            valid.append(x)
    for i in range(1,len(valid)-1):
        prev= valid[i-1]
        curr=valid[i]
        next=valid[i+1]
        best_window=[prev,curr,next]
        maximum_three_day_sum=prev+curr+next
        if maximum_three_day_sum>largest:
            maximum_three_day_sum=maximum_three_day_sum
            best_window=[prev,curr,next]
    return{"List of valid values":valid,
           "Maximum sum of 3 consicutive days":maximum_three_day_sum,
           "List of Max sum window":best_window}
data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=analyze_values(data)
for key, value in result.items():
    print(f"{key}:{value}")
