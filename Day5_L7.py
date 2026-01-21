div_by_3=[]
div_by_5=[]
div_by_both=[]
nums = [15, 22, 30, 45, 60, 7, 9]
for x in nums:

    if x%3==0:
        div_by_3.append(x)
    if x%5==0:
        div_by_5.append(x)
    if x%3==0 and x%5==0:
        div_by_both.append(x)
   
print("Numbers divisible by 3:->",div_by_3)
print("Numbers divisible by 5:->",div_by_5)
print("Numbers divisible by both 3 and 5",div_by_both)