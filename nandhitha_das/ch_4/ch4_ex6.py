# program to print pay using try and except
# ex3.11 pg 52

try:
    hours_worked = int(input("Enter hours: "))
except:
    print("Error, please enter hours as a numeric input")
    exit(0)

try:
    basic_rate_per_hour = int(input("Enter rate: "))
except:
    print("Error, please enter basic rate as a numeric input")
    exit(0)

# defining a function named compute_pay
# the function will take two parameters hours_worked and basic_rate_per_hour
def compute_pay(hours_worked, basic_rate_per_hour):
    minimum_work_hour = 40
    extra_time_multipler = 1.5

    extra_time_wage_per_hour = basic_rate_per_hour * extra_time_multipler
    total_work_hours = hours_worked - minimum_work_hour

    total_wages_for_extra_time = total_work_hours * extra_time_wage_per_hour
    total_wages_for_minimum_time = minimum_work_hour * basic_rate_per_hour
    total_pay = total_wages_for_minimum_time + total_wages_for_extra_time
    return total_pay

final_total_pay = compute_pay(hours_worked, basic_rate_per_hour)
print("Final total pay : ", final_total_pay)

