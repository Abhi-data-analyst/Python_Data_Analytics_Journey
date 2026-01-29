def corrected_list(simple_range):
    new_list=[]
    for x in simple_range:
        if x==-1:
            continue
        else:
            new_list.append(x)
    return new_list

simple_range = [-1, 8, 0, 2, 19, 20, 5, 12, 7, 14, 0, -1, 20, -1, 9]
result=corrected_list(simple_range)
print(result)