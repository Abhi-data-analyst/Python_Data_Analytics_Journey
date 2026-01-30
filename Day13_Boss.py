def monthly_data(monthly_sale):
    total_sales=0
    best_day_sale=0
    worst_day_sale=999
    count_sale_days=0
    count_of_nosale_days=0
    for x in monthly_sale:
        if x==-999:
            continue
        if x==0:
            count_of_nosale_days+=1
            continue
        if x>0:
            total_sales+=x
            count_sale_days+=1
        if x>best_day_sale:
            best_day_sale=x
        if x<worst_day_sale:
            worst_day_sale=x
    avg_valid_sale=total_sales/count_sale_days
    return {"Average sale":avg_valid_sale, "Total sale":total_sales, "Best Sale day":best_day_sale, "Worst day sale":worst_day_sale, "Number of Nosale days":count_of_nosale_days}
monthly_sales = [
    120, 150, 0, 45, -999, 88, 195, 
    0, 22, 110, -999, 0, 75, 130,   
    180, 15, 0, 99, 200, -999, 40,   
    65, 0, 125, 33, 115, 0, 190,     
    10, 55                           
]
print(monthly_data(monthly_sales))