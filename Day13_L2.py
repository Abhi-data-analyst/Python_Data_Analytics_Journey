def data_cotegry(test_data_200):
    low=[]
    medium=[]
    high=[]
    for x in test_data_200:
      if x<50:
        low.append(x)
      if 50<=x<=100:
        medium.append(x)
      if x>100:
        high.append(x)
    return low , medium , high
    
test_data_200 = [
    12, 145, 67, 190, 44, 82, 110, 5, 50, 155, 
    22, 98, 125, 33, 71, 188, 49, 101, 60, 130,
    15, 88, 175, 40, 200
]
result=data_cotegry(test_data_200)
print(result)