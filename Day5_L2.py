total_sale=0
valid_sale=0
largest=0
smallest=9999
avg_sale=0
sales = [1200, 0, 450, 0, 800, 300, 0, 1500] 
for x in sales:
    if x==0:
        continue
    if x>0:
        valid_sale+=1
        total_sale+=x
    if    x>largest:
        largest=x
    if  x<smallest:
        smallest=x
avg_sale=total_sale/valid_sale

print("The highest value of sale in the list is:-",largest)
print("The least value of sale in the list is:-",smallest)
print("Total sales as per the list is:-",total_sale)
print("Average sales per day excluding no sale days:-",avg_sale)
