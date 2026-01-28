def sales_analysis(list):
    refund_count=0
    sale_count=0
    refund_sum=0
    sale_sum=0
    for x in list:
        if x ==0:
            continue
        if x>0:
            sale_count+=1
            sale_sum+=x
        else:
            refund_count+=1
            refund_sum+=x
    net=(sale_sum-(-refund_sum))
    return refund_count,refund_sum,sale_count,sale_sum,net
list1 = [1200, 1500, -1000, 0, 2200, 1800, -2500, 3000, 2500,100]                                         
list2=  [2200, 2300, 2100, -1900, 2400, 2500, -1500, -2200, 2100]
list3 = [4500, -1000, 0, -1500, 5200, 610, -10, -5500, 4500, 950]
print(sales_analysis(list1))
print(sales_analysis(list2))
print(sales_analysis(list3))