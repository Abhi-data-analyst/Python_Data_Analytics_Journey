def sales(monthly_sales):
    error_days=0
    zero_sale_days=0
    valid_sale_days=0
    sale_value=0
    for x in monthly_sales:
        if x ==-1:
            error_days+=1
            continue
        if x ==0:
            zero_sale_days+=1
        if x >0:
            valid_sale_days+=1
            sale_value+=x
    avg=sale_value/valid_sale_days
    return error_days,zero_sale_days,valid_sale_days,avg
monthly_sales = [
    45, 52, 60, -1, 0, 88, 92,  
    34, 41, 55, 62, 0, 0, 105,  
    48, 50, -1, 15, 22, 98, 112, 
    39, 44, 0, 25, -1, 82, 95,   
    42, 51                       
]
print(sales(monthly_sales))