weekly_sales = [
    [10, -1, 20, 0],
    [0, 15, -1, 25],
    [30, 0, 5, -1]
]
valid_count=0
zero_count=0
valid_sum=0
for region in weekly_sales:
    for x in region:
        if x==-1:
            continue
        if x==0:
            zero_count+=1
        if x>0:
            valid_count+=1
            valid_sum+=x
print("valid count:->",valid_count)
print("zero count:->",zero_count)
print("Sum of valid values:->",valid_sum)