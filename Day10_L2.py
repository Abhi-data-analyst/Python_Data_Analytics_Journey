def valid_sum(sales):
    total=0
    for x in sales:
        if x==-1:
            continue
        else:
            total+=x
    return total
sales = [
    45, 52, 0, 12, -1, 88, 92, 
    34, 41, 0, 55, 62, -1, 105, 
    48, 50, 0, 15, 22, 98, 112, 
    39, 44, 0, 25, -1, 82, 95,  
    42, 51, 0                   
]
print(valid_sum(sales))