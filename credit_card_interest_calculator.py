balance_due = float(input("Enter the balance due: "))
rate_of_interest = float(input("Enter the rate of interest: "))

monthly_expense = float(input("Enter the monthly payment: "))

#number_of_months = int(input("Enter the number of months you want to keep the payment: "))

total_interest = 0

months = ["May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
for month in months:
    balance_due = balance_due - monthly_expense + total_interest
    interest_on_balance = balance_due * rate_of_interest / 100
    balance_after_expense_made = balance_due + monthly_expense
    interest_on_balance_after_expense = balance_after_expense_made * rate_of_interest / 100
    interest_on_expense = monthly_expense * rate_of_interest / 100
    total_interest = interest_on_balance + interest_on_balance_after_expense + interest_on_expense
    balance_due = balance_after_expense_made

    print("\n")
    print("Total interest this month: " + str(total_interest))
    print("Balance carried over to " + month + ": "  + str(balance_due))

print("\n")
print("Final balance after paying off the monthly expense: " + str(balance_due - monthly_expense))
print("Total interest incurred: " + str(total_interest))
