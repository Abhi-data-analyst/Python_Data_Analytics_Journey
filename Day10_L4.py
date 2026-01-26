def analyz_marks(marks):
    count=0
    total=0
    for x in marks:
        if x <=0:
            continue
        else:
            count+=1
            total+=x
    avg=total/count
    return(count,total,avg)
marks=[60, 65, 70, 75, 0, 0, 120, 130, 140, 150, 0, 0, 85, 90, 
    95, 100, -1, 0, 180, 190, 200, 210, 0, 0, 55, 60, 65, 70, 75
]
print(analyz_marks(marks))