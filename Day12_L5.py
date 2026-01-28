def region_wise(sale):
    highest=0
    total=0
    count=0
    for x in sale:
        if x <=0:
            continue
        else:
            total+=x
            count+=1
        if x>highest:
            highest=x
    avg=total/count
    return highest,avg
region_north_sale = [1200, 1500, -1, 0, 2200, 1800, -1, 3000, 2500, 0]
region_south_sale = [220, 2300, 21, -99, 2400, 2500, -1, 2200, 2100]
region_west_sale = [4500, 0, 0, 0, 5200, 610, 0, 0, 4500, 950]
region_east_sale = [500, 4500, 1000, 2000, -1, 5000, 0, 3000, 4250, 500]
export_sale = [700, 900, 0, 550, 0, 600, 700, 4500, 8000, 10000]
print(region_wise(region_east_sale))
print(region_wise(region_west_sale))
print(region_wise(region_south_sale))
print(region_wise(region_north_sale))
print(region_wise(export_sale))