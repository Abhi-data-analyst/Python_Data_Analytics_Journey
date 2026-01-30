def value_check(test_data):                                  
   count_invalid=0
   count_valid=0                                                            
   sum_valid=0
   for x in test_data:
        if x<=0:                                                        
           count_invalid+=1                                                
           continue                                                        
        else:                                                                
         count_valid+=1                                                             
         sum_valid+=x                                              
   valid_avg= sum_valid/count_valid
   return {"Average":valid_avg, "Valid":count_valid,"Invalid":count_invalid,"Sum":sum_valid }
test_data = [
    -1, 145, 67, 0, 44, 82, 110, 5,0, 155, 
    22, 98, 125, 33, 71, 188, 49, -1,-1, 60, 130,
    15, 88, 175, 40, 0
]
result=value_check(test_data)
print(result)