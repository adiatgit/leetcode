prices = [2,4,1]
meh = msf = 0
for i in range(1, len(prices)):
    meh = meh + prices[i] - prices[i - 1]
    meh = max(0, meh)
    msf = max(msf, meh)
print(msf)