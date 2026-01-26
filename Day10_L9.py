def count(sales,threshold):
    count=0
    for x in sales:
        if x <=0:
            continue
        elif x>threshold:
            count+=1
    return count
sales = [500, 1200, 0, 1800, -1, 700, 2500]
threshold = 1000
print(count(sales,threshold))