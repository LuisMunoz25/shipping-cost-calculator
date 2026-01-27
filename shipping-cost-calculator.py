# Define a weight variable and set it to any number
weight = float(input("Enter the weight of the package in pounds: "))
cost_ground = ""
ground_shipping_premium = 125
drone_shipping = ""


# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# Ground shipping
if weight <= 2:
  cost_ground = "The ground shipping fee is: $" + str(round(weight * 1.50 + 20, 2))
elif weight > 2 and weight <= 6:
  cost_ground = "The ground shipping fee is: $" + str(round(weight * 3.00 + 20, 2))
elif weight > 6 and weight <= 10:
  cost_ground = "The ground shipping fee is: $" + str(round(weight * 4.00 + 20, 2))
else:
  cost_ground = "The ground shipping fee is: $" + str(round(weight * 4.75 + 20, 2))

# Write a comment for this section of the code, “Drone Shipping”.
# Drone Shipping
if weight <= 2:
  drone_shipping = "The drone shipping fee is: $" + str(round(weight * 4.50, 2))
elif weight > 2 and weight <= 6:
  drone_shipping = "The drone shipping fee is: $" + str(round(weight * 9.00, 2))
elif weight > 6 and weight <= 10:
  drone_shipping = "The drone shipping fee is: $" + str(round(weight * 12.00, 2))
else:
  drone_shipping = "The drone shipping fee is: $" + str(round(weight * 14.75, 2))

print(cost_ground)
print("Ground Shipping Premium is $" + str(round(ground_shipping_premium, 2)))
print(drone_shipping)