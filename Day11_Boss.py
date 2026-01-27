def value(transaction_ledger):
    refund_count=0
    total_refund_amount=0
    total_sales_amount=0
    for x in transaction_ledger:
        if x==-999:
            continue
        if x<0:
            refund_count+=1
            total_refund_amount+=x
        else:
            total_sales_amount+=x
    net_balance=(total_sales_amount-(-total_refund_amount))
    return refund_count,total_sales_amount,total_refund_amount,net_balance
transaction_ledger = [
    500,-999, -150, 200,-999, -50, 1000, -300, 450, -20, 150, 800, -500, 100,544
]
print(value(transaction_ledger))