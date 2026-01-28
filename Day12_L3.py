def profit_loss(sales):
    profit=0
    loss=0
    for x in sales:
        if x==-999:
            continue
        if x>0:
            profit+=x
        if x<0:
            loss+=x
    net= (profit-(-loss))
    return profit, loss, net
sales=[500,700,-250,-750,250,550,-500,-999,750,-120]
print(profit_loss(sales))
        
