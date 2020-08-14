principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
i = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
#    print(month)
    while month < 12:
 #       print("before", month)
        principal = principal * (1+rate/12) - (payment+1000)
        total_paid = total_paid + (payment+1000)
        i += 1
        month += 1
#        print("after", month)
#        print(i)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month +=1

print('Total paid', total_paid, month)
