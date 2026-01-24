def valid_sum(marks):
    sum=0
    for x in marks:
        if x <=0:
            continue
        else:
            sum+=x
    return sum
marks=[45,45,65,-1,-9,0,69,0,0,15]
print(valid_sum(marks))
    