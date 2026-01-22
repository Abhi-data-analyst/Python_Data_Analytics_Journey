highest=0
lowest=9999
total=0
valid_sale=0
no_sale=0
sales = [0, 1200, 800, -1, 0, 500, 1500, -1, 300]
for x in sales:
    if x<0:
        continue
    elif x==0:
        no_sale+=1
    else:
        valid_sale+=1
        total+=x
        if x>highest:
            highest=x
        elif x<lowest:
            lowest=x
avg= total/valid_sale
print("Number of valid sale days:->",valid_sale)
print("Number of no sale days:->",no_sale)
print("Highest sale in one day:->",highest)
print("Lowest sale in one day:->",lowest)
print("Average sales:->",avg)
