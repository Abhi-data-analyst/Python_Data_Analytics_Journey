def merge_valid(list_source):
    valid_count=0
    valid_sum=0
    highest=0
    lowest=99
    merged_list=[]
    for x in list_source:
        if x <=0:
            continue
        else:
            valid_count+=1
            valid_sum+=x
            merged_list.append(x)
        if x >highest:
            highest=x
        if x< lowest:
            lowest=x
    avg=valid_sum/valid_count
    return{"Highest value ":highest,"lowest value":lowest,"Average of all valid values":avg,"New list":merged_list}
list_source_A = [15, 85, -1, 42, 0]
list_source_B = [120, 0, 95, -1, 10]
list_source_C = [55, 180, 0, 30, -1]
list_source= list_source_A +list_source_B + list_source_C
print(merge_valid(list_source))
