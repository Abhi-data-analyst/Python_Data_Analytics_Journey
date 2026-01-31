def machine_runtime(runtime_data):
    total_active_days=0
    total_runtime=0
    idle_days=0
    list_heavy_usage_days=[]
    for x in runtime_data:
        if x ==-1:
            continue
        if x==0:
            idle_days+=1
            continue
        else:
            total_active_days+=1
            total_runtime+=x
    avg=total_runtime/total_active_days
    for x in runtime_data:
        if x>avg:
            list_heavy_usage_days.append(x)
    return{"Number of active days":total_active_days,
           "Total runtime":total_runtime,
           "Number of Idle days":idle_days,
           "New list of heavy usage days":list_heavy_usage_days}
runtime_data = [
    -1, 5, 0, 8, 12, -1, 0, 15,
    3, 7, 0, 20, -1, 4, 9
]
result=machine_runtime(runtime_data)
for key, value in result.items():
    print(f"{key}:{value}")
