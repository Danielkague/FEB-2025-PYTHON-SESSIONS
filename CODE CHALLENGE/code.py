#question 1
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discounted_price = price - (price * discount_percent / 100)
        print(discounted_price)
    else:
        print(price)

calculate_discount(100, 10)
calculate_discount(69, 20)
calculate_discount(40, 30)
calculate_discount(200, 5)

#question 2
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discounted_price = price - (price * discount_percent / 100)
        print(discounted_price)
    else:
        print(price)
price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)

