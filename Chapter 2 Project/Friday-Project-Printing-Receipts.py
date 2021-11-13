

#Python Projects for Beginners
#Python Coding Bootcamp | Chapeter 2 | Project: Creating a Receipt Printing Program

#create top border of receipt 
print('*'* 50)
#print("\n")
#create company name and information
company_name = "coding temple, inc."
company_address = "283 franklin street"
company_state = "Boston, MA" 

#test company name and information using print statement, test successful
#print(company_name,company_address, company_state)
print("\n \t \t{}".format(company_name.title()))#title method, capitalize first letter of each word in string
print("\t \t{}".format(company_address.title()))
print("\t \t{} \n".format(company_state))
#test successful

#create bottom border for company information. This line seperates company address from product name and product  price section

print("=" * 50)
#column for product name
print("\n\tProduct Name\tProduct Price\n")

# define variables for products. 3 items: Books, Computer and Monitor

product_1_name = "Books"
product_2_name = "Computer"
product_3_name = "Monitor"

product_1_price = 49.95 #add $ sign before price : print("\t{}\t\t${}".format(product_1_name,product_1_price))
product_2_price = 579.99
product_3_price = 124.89

#test product names using print statement
#print(product_1_name, product_2_name, product_3_name), test successful
print("\t{}\t\t${}".format(product_1_name,product_1_price)) #error tried to print variable before it was declare, ""not define""
print("\t{}\t${}".format(product_2_name,product_2_price))
print("\t{}\t\t${}\n".format(product_3_name,product_3_price))

#test product prices using print statement
#print(product_1_price, product_2_price, product_3_price)

#print("\t{}".format(product_1_price))
#print("\t{}".format(product_2_price))
#print("\t{}".format(product_3_price))

#create top border for price total
#new line spacing

print("=" * 50)

#define variable for total cost of 3 products
#header for total cost
print("\n\t\t\tTotal")
total_cost = product_1_price + product_2_price + product_3_price
#put dollar sign before variable 'total_cost' : print("${}".format(total_cost))
print("\n\t\t\t${}\n".format(total_cost))

#test cost variable

# test: does total_cost variable print: print(total_cost), test successful

#create bottom border for price total

print("=" * 50)

#receipt ending message  
message = "Thanks for shopping with us today!"
#print message
#space above print message
#test if message prints
#print(message)
print("\n")
print("\t{}".format(message))
#space below print message
print("\n")
#bottom border for receipt
print("*" * 50)
