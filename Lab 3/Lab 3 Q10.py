#Question 10

amount=float(input('Enter purchase amount '))

discount=0

if amount>5000:
    discount=amount*0.20
elif amount>2000:
    discount=amount*0.1
else:
    discount=0

final_amount=amount-discount

print('Final Amount to Pay:', final_amount)
