def trend_analysis(data):
    valid=[]
    for x in data:
        if x>0:
            valid.append(x)
    count_up=0
    count_down=0
    no_of_trend_changes=0
    trend_change_list=[]
   
    for i in range(1,len(valid)):
        prev=valid[i-1]
        curr=valid[i]
       
        if prev==curr:
            continue
        elif prev<curr:
            count_up+=1
            
            trend_change_list.append("UP")
        else:
            count_down+=1
            
            trend_change_list.append("Down")
        if prev<curr or prev>curr:
            no_of_trend_changes+=1
    return{"valid list":valid,
           "List of trends":trend_change_list,
           "Number of trend changes":no_of_trend_changes}

data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=trend_analysis(data)
for k, v in result.items():
    print(f"{k}:{v}")
