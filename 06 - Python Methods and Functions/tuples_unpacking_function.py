stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

# using for loops
for item in stock_prices:
    print(item)

for code, price in stock_prices:
    # 10% increase
    print(price + (0.1 * price))

# using function
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]


def employee_check(work_hours):
    # placeholder variables
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Return
    return employee_of_month, current_max


employee_of_the_month = employee_check(work_hours)
name, hours = employee_check(work_hours)

print(employee_of_the_month)

print(hours)
print(name)
