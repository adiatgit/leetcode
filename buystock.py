def buystock(prices):
    lprice = float('inf')
    hprice = float('-inf')

    for each_price in prices:
        if each_price > hprice:
            hprice = each_price
        elif lprice < each_price:
            lprice = each_price
            hprice = each_price
    if hprice - lprice > 0:
        return hprice - lprice
    return 0
print(buystock([7,1,5,3,6,4]))