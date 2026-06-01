product_name = str(input("Enter the product name: "))
unit_cost =int(input("Enter the unit cost: "))
quantity = int(input("Enter the quantity: "))

print(product_name)

total_cost = unit_cost * quantity
print("Total cost: ", total_cost)

# discount calculation
product_price = int(input("Enter the product price: "))
dicount_percentage = int(input("Enter the discount percentage: "))

discount_amount = (product_price * dicount_percentage) / 100
final_price = product_price - discount_amount

print("Final price after discount: ", final_price)
print("Discount amount: ", discount_amount)

# GST billing system
subtotal = unit_cost * quantity
gst_amount = subtotal * 0.18
final_bill = subtotal + gst_amount

print("Subtotal: ", subtotal)
print("GST Amount: ", gst_amount)
print("Final Bill: ", final_bill)


# Retail Profile analysis
seller_price = int(input("Enter the selling price: "))
unit_sold = int(input("Enter the units sold: "))

revenue = seller_price * unit_sold
print("Revenue: ", revenue)

cost_price = int(input("Enter the cost price: "))

investment = cost_price * unit_sold
print("Investment: ", investment)


profit = revenue - investment
print("Profit: ", profit)

profit_percentage = (profit / investment) * 100
