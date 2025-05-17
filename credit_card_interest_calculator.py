balance_due = float(input("Enter your starting balance (e.g. 21000): "))
rate_of_interest = float(input("Enter monthly interest rate (%) (e.g. 3.75): "))
monthly_payment = float(input("Enter how much you pay (and spend again) each month (e.g. 13000): "))

months = ["June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
total_interest = 0

for month in months:
    # 1. Interest applies to balance (including past interest)
    interest = balance_due * (rate_of_interest / 100)
    balance_due += interest  # Interest gets added to balance
    total_interest += interest

    # 2. Pay 13,000
    balance_due -= monthly_payment

    # 3. Spend 13,000 again
    balance_due += monthly_payment

    # At the end of the cycle balance is previous balance + all previous interest!
    print(f"{month}: interest charged: {interest:.2f}, total owed now: {balance_due:.2f}")

print(f"\nTotal interest paid by December: ₹{total_interest:.2f}")
print(f"Balance still remaining in December: ₹{balance_due:.2f}")