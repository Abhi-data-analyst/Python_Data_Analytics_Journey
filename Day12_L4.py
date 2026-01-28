def extreme_values(marks):
    highest=0
    lowest=999
    for x in marks:
        if x<=0:
            continue
        else:
            if x>highest:
                highest=x
            if x<lowest:
                lowest=x
    return highest, lowest
marks = [
    85, 92, 0, 78, -1, 45, 100,66, 0, 
    89, -1, 55, 94, 0, 72, 81, -1, 33, 98, 0, 50, 88
]
print(extreme_values(marks))