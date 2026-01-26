def valid_avg(numbers):
    even_count=0
    valid_total=0
    for x in numbers:
        if x <=0:
            continue
        if x%2==0:
            even_count+=1
            valid_total+=x
    avg=valid_total/even_count
    return avg,even_count,valid_total
numbers = [12, 15, 0, 8, -2, 20, 7, 14]
print(valid_avg(numbers))
