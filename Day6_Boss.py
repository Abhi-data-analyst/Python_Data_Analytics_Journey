region_list = ["North", "South", "East"]
regional_sales = [
    [500, -1, 200, 0, 800],    
    [0, 0, 1500, -1, 300],     
    [1000, 400, 600, -1, 0]    
]

highest_sale_amount = 0
winner_name = ""

for i in range(len(regional_sales)):
    region_name = region_list[i]
    sales_data = regional_sales[i]
    
    current_total = 0
    for sale in sales_data:
        if sale > 0:
            current_total += sale
            
    # PRINT HERE (Outside inner loop, inside outer loop)
    print(f"{region_name} Total Sales: {current_total}")
    
    # WINNER LOGIC (Using the logic you mastered in Task 6.3)
    if current_total > highest_sale_amount:
        highest_sale_amount = current_total
        winner_name = region_name

print("-" * 20)
print(f"Winner: {winner_name} with ${highest_sale_amount}")