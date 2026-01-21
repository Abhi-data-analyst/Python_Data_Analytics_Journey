div_by_3=[]
div_by_5=[]
div_by_both=[]
numbers = [10, 15, 22, 30, 45, 60, 7, 9]
for x in numbers:
    if x%3==0 and x%5==0:
        div_by_both.append(x)
    if x%3==0:
        div_by_3.append(x)
    if x%5==0:
        div_by_5.append(x)
print("These numbers are divisible by 3 and 5:-",div_by_both) 
print("These numbers are divisible by 3:-",div_by_3)
print("These numbers are divisible by 5:-",div_by_5)