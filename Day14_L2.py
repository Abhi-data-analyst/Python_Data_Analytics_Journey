def reading(energy_consuption_readings):
    valid_con=0
    total_valid_con=0
    idle_days=0
    high_usage=[]
    for x in energy_consuption_readings:
        if x==-1:
            continue
        if x>0:
            valid_con+=1
            total_valid_con+=x
        if x==0:
            idle_days+=1
    avg= total_valid_con/valid_con
    for x in energy_consuption_readings:
        if x>avg:
            high_usage.append(x)

    return {"Valid consuption days": valid_con,
             "Total valid consuption":total_valid_con,
             "Number of idle days":idle_days,
               "Average consuption of valid days": avg,
                 "List of high usage days":high_usage
                 }

energy_consuption_readings = [
    -1, 0, 100, 45, -1, 0, 88, 12, -1, 99,
    0, 75, 1, 0, -1, 50, 66, -1, 0, 92
]
print(reading(energy_consuption_readings))