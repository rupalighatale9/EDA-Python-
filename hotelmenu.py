# Define the menu of Restaurant
menu = {
    "Pizza":90,
    "Pasta":70,
    "Burger":80,
    "Manchurian":50,
    "Noddles":50,
    "Salad":70,
    "Cold coffe":80,
    "Chocholate Tea":20,
    "Peri Peri Fries":70,
    "Sandwich":90,
    "coffe":20,
    "Fried Rice":60,
}
print(menu)
#Greet
print(" Welcome to Rupali's Restaurant ")
print("Pizza: Rs90\n Pasta:70\n Burger:Rs80\n Manchurian:Rs50\n Noddles:Rs50\n Salad:70\n Cold coffe:80\n"
       "Chocholate Tea:Rs20\n Peri Peri Fries:Rs70\n Sandwich:Rs90\n coffe:20\n Fried Rice:Rs60")

order_total = 0
#80 + 70 =150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want add another item?  (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print("Ordered item {item_2} is not available! ")

print(f"The total amount of items to pay is {order_total} ")
