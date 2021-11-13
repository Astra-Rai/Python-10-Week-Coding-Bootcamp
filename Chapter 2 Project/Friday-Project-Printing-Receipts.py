
#Python Projects for Beginners
#Python Coding Bootcamp | Chapeter 2 | Project: Creating a Receipt Printing Program
#create top border of receipt 
print("*" * 50)

#create company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin Street"
company_state = "Boston, MA" 

#test company name and information using print statement

print(company_name,company_address, company_state)

#test successful

#create bottom border for company information. This line seperates company address from product name and product  price section

print("=" * 50)

# define variables for products. 3 items: Books, Computer and Monitor

product_1_name = "Books"
product_2_name = "Computer"
product_3_name = "Monitor"

#test product names using print statement

print(product_1_name, product_2_name, product_3_name)

#test successful 


product_1_price = 49.95
product_2_price = 579.99
product_3_price = 124.89

#test product prices using print statement

print(product_1_price, product_2_price, product_3_price)

#create top border for price total

print("=" * 50)

#define variable for total cost of 3 products

total_cost = product_1_price + product_2_price + product_3_price
#put dollar sign before variable 'total_cost'
print("${}".format(total_cost))

#test cost variable

print(total_cost)

#create bottom border for price total

print("=" * 50)

#receipt ending message  

message = "Thanks for Shopping with us today!"

#print message

print(message)