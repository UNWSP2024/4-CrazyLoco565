budget = float(input("Enter your budget for the month: "))

total_expenses = 0

while True:
    expense = input("Enter an expense amount (or type 'done' to finish): ")
    if expense.lower() == "done":
        break
    total_expenses += float(expense)

if total_expenses > budget:
    print(f"\nYou are OVER budget by ${total_expenses - budget:.2f}")
elif total_expenses < budget:
    print(f"\nYou are UNDER budget by ${budget - total_expenses:.2f}")
else:
    print("\nYou are exactly ON budget!")
