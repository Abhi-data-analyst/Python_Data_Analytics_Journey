def new_value(data):
    total_valid_days=0
    current_up=0
    current_down=0
    current_same=0
    max_up=0
    max_down=0
    max_same=0
    valid=[]
    for x in data :
        if x <=0:
            continue
        if x>0:
            total_valid_days+=1
            valid.append(x)
    for i in range (1, len(valid)):
            prev = valid[i-1]
            curr = valid[i]
            if prev < curr:
               current_up+=1
               current_down=0
               current_same=0
               max_up= max(max_up, current_up)
            elif prev == curr:
                 current_same+=1
                 current_down=0
                 current_up=0
                 max_same = max(max_same, current_same)

            else:
                 current_down+=1
                 current_up=0
                 current_same=0
                 max_down = max(max_down, current_down)
    return{"Number of valid days":total_valid_days,
           "Longest Up streak":max_up,
           "Longest down streak":max_down,
           "Longest same streak":max_same,
           "Total up":current_up,
           "Total down":current_down,
           "Total same":current_same}

data = [45, 78, 78, -1, 65, 88, 0, 55, 100, 34, -1, 80, 80, 95]
result=new_value(data)
for key, value in result.items():
    print(f"{key}:{value}")
