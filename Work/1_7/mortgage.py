#!/usr/bin/env python3
# 固定年利率
rate = 0.05
# 总贷款金额
principal = 500000
# 贷款时间
month = 30 * 12
# 每月还款
payment = 2684.11
# 总还款
total = 0.0

while principal > 0:
    principal = principal + principal * rate / 12 - payment
    total = total + payment
    month = month - 1

print(total, month)

rate = 0.05
principal = 500000
month = 30 * 12
payment = 2684.11
total = 0.0
extra_payment = 1000
extra_month = 12
while principal > 0:
    principal = principal + principal * rate / 12 - payment
    if extra_month > 0:
        principal = principal - extra_payment
        total = total + extra_payment
        extra_month = extra_month - 1

    total = total + payment
    month = month - 1

print(total, month)

rate = 0.05
principal = 500000
month = 1
payment = 2684.11
total = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
while principal > 0:
    principal = principal + principal * rate / 12 - payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total = total + extra_payment
        extra_month = extra_month - 1
    if principal < 0:
        print("last month: ", principal)
        payment = payment + principal
    total = total + payment
    print(month, total)
    month = month + 1

print("Total paid", total)
print("Months", month)
