def classify_performance(performance_scores):
    low_performance=[]
    mid_performance=[]
    high_performance=[]
    valid_score_count=0
    for x in performance_scores:
        if x ==-1:
            continue
        else:
            valid_score_count+=1
        if x<49:
            low_performance.append(x)
        if 50<x<79:
            mid_performance.append(x)
        if x>80:
            high_performance.append(x)
    return{"List of low performance days":low_performance,
           "List of mid performance days":mid_performance,
           "List of high performance days":high_performance,
           "Number of valid days":valid_score_count}
performance_scores = [
    45, 78, -1, 90, 33, 67, 82,
    0, -1, 55, 40, 99, 73, -1, 88
]
result=classify_performance(performance_scores)
for key, value in result.items():
    print(f"{key}:{value}")


