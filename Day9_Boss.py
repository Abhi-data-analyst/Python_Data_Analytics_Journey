def valid_avg(sales):
    valid_count=0
    valid_total=0
    for x in sales:
        if x ==-1:
            continue
        else:
            valid_count+=1
            valid_total+=x
    avg=valid_total/valid_count
    return (avg)
week1_sales = [450, 700, 0, 1200, -1, 850, 1000]
week2_sales = [1500, 2100, -1, 1800, 0, 2500, -1]
week3_sales = [300, -1, 0, 450, 350, 0, 500]
print(valid_avg(week1_sales))
print(valid_avg(week2_sales))
print(valid_avg(week3_sales))