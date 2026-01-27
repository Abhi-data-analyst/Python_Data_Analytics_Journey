def sale(sales_volatile):
    total_sale=0
    valid_sale=0
    zero_sale=0
    for x in sales_volatile:
        if x==-1:
            continue
        if x==0:
            zero_sale+=1
        else:
            valid_sale+=1
            total_sale+=x
    avg=total_sale/valid_sale
    return valid_sale, total_sale, avg
sales_volatile = [450, 520, -1, -1, -1, 0, 890, 1100, -1, -1, 0, 430]
print(sale(sales_volatile))