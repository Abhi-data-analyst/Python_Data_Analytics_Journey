sale_day=0
no_sale_day=0
total_sale=0
sales = [0, 1200, 800, -1, 0, 500, 1500, -1, 300]
for x in sales:
    if x==-1:
        continue
    if x>0:
        sale_day+=1
        total_sale+=x
    if x==0:
        no_sale_day+=1
avg_sale= total_sale/sale_day
print("Number of sale days:->",sale_day)
print("Number of no sale days:->",no_sale_day)
print("Total sale:->",total_sale)
print("Average sales per sales day:->",avg_sale)

