from time import gmtime, strftime

store_name="NotaReal Supermarket"
store_website="www.notarealsupermarket.net"

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

#print(products)


product_ids=[]
while True:
    item=input("Please input a product ID, or 'DONE' if there is no more items: ")
    if item == 'DONE':
        break
    if not item.isdigit():
        print("You must enter a number")
    if int(item) not in range(1,21):
        print("Please enter a number from 1 to 20 only")
    else:
        product_ids.append(int(item))
#print(product_ids)


print('\n')
print('-----------------------------')
print(store_name)
print('-----------------------------')
print(store_website)
print('Check out time: ', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print('-----------------------------')
print('\n')

#print(products)

#product_ids = [1, 8, 6, 16, 6] # temporary list of valid ids for testing purposes


print('-----------------------------')
print('Shopping cart item: ')
#TODO: perform product look-ups here!
def name_and_price(id):
    for transaction in range(len(products)):
        if products[transaction]['id']==id:
            name= products[transaction]['name']
            price= products[transaction]['price']
    return name,price

total_price=0
for id in product_ids:
    name,price= name_and_price(id)
    print('+ ',name, ' ', price)
    total_price+=price
print('-----------------------------')
print('THE TOTAL PRICE IS: $',round(total_price,2))
print('THE TAX RATE IS: $', round(.06*total_price,2))
print('TOTAL AMOUNT OWNED: $', round(1.06*total_price,2))
print('\n')
print('THANK YOU VERY MUCH FOR SHOPPING AT NOTAREAL Supermarket! I HOPE YOU COME BACK SOON!')


