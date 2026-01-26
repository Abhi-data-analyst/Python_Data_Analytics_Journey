def result(store_a,store_b,store_c):
    valid_count=0
    invalid_count=0
    total=0
    max_value=0
    for store in (store_a, store_b,store_c):
        for x in store:
            if x<0:
             invalid_count+=1
             continue
            if x>0:
             valid_count+=1
             total+=x
            if x>max_value:
             max_value=x

    average=total/valid_count        
    return invalid_count,valid_count,average,max_value
store_a = [1200, 1500, 0, -1, 1800, 2100, 0]
store_b = [500, 0, 700, 800, -1, 900]
store_c = [300, 450, 0, 0, 600, 750]
print(result(store_a,store_b,store_c))
