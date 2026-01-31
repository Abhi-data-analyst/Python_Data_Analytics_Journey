def analyze_sales(sales_data):
    total_valid_days=0
    total_sales_amount=0
    no_sale_days=0
    high_sale_list=[]
    low_count=0
    mid_count=0
    high_count=0
    for x in sales_data:
        if x==-1:
            continue
        else:
            total_valid_days+=1
            total_sales_amount+=x
        if x==0:
            no_sale_days+=1
            continue
        if 99>x>1:
            low_count+=1
        elif 299>x>100:
            mid_count+=1
        else:
            high_count+=1
            high_sale_list.append(x)
    return{"Number of valid days":total_valid_days,
           "Total sales amount": total_sales_amount,
           "Number of no sale days":no_sale_days,
           "Number of Low sales days":low_count,
           "Number of medium sale days":mid_count,
           "Number of high sale days":high_count,
           "List for only high sale days":high_sale_list}
sales_data = [
    120, 0, 450, -1, 75, 300, 0, 220,
    -1, 90, 600, 50, 10, 0, 305
]
result=analyze_sales(sales_data)
for key, value in result.items():
    print(f"{key}:{value}")

