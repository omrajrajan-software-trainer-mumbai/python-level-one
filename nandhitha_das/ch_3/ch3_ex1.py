#Program to compute pay for workers
#exercise 3.11 pg 40

total_hours_worked = int(input("Enter hours: ")) #interactive-taking value from user
basic_wage_per_hour = int(input("Enter rate: ")) #interactive-taking value from user

minimum_work_hours = 40 #hard-coded
extra_time_multiplied = 1.5 #hard-coded

#assume that the total_hours_worked user entered is 45
#assume that the basic_wage_per_hour user entered is 10

extra_time_wage_per_hour = basic_wage_per_hour * extra_time_multiplied
extra_hours = total_hours_worked - minimum_work_hours

total_wage_for_extra_time = extra_time_wage_per_hour * extra_hours
total_wage_for_minimum_time =  minimum_work_hours * basic_wage_per_hour
total_pay = total_wage_for_extra_time + total_wage_for_minimum_time
print("Total pay: ",total_pay)
