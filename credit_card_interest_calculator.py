balance_due = float(input("Enter the balance due: "))
rate_of_interest = float(input("Enter the rate of interest: "))

monthly_payment = float(input("Enter the monthly payment: "))

number_of_months = int(input("Enter the number of months you want to keep the payment: "))

total_interest = 0
balance_due_this_month = 0
for i in range(number_of_months):
    balance_due = balance_due - monthly_payment + total_interest
    balance_interest = balance_due_this_month * (1 + (rate_of_interest / 100))
    payment_interest = monthly_payment * (1 + (rate_of_interest / 100))
    net_interest_this_month = balance_interest + payment_interest
    total_interest = net_interest_this_month

print("Total interest incurred: " + str(total_interest))