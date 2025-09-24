years = int(input("Enter number of years: "))

total_rainfall = 0
months = years * 12

for year in range(1, years + 1):
    print(f"\nYear {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall (in inches) for month {month}: "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / months

print("\nResults:")
print(f"Number of months: {months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

