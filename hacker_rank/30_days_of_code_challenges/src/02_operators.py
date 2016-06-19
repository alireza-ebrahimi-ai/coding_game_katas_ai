meal_cost = float(input())
tip_percent = float(input())
tax_percent = float(input())

print("The total meal cost is " + str(round(meal_cost + (meal_cost * tip_percent / 100) + meal_cost * tax_percent / 100))  + " dollars.")