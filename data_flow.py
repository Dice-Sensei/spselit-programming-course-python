is_true = True  # je to pravda
is_false = False  # není to pravda

# bool / boolean

# user_input = input("Write 'car': ")
# print("You wrote:", user_input)
# print("it was car", user_input == "car")

# porovnávat pouze stejné datové typy
# user_input = input("Your age: ")
# print("You wrote:", user_input)
# print(
#     "we are same old", int(user_input) == 30
# )  # int() zajištuje konverzi stringu na číslo aby porovnání mohlo proběhnout správně

# 3 != 4 # používanější varianta
# not (3 == 4)
# print("Is 3 != 4 ?", not (3 == 4))

# print("Is 4 larger then 3?", 4 > 3)
# print("Is 4 larger or equal to 3?", 4 >= 3)
# print("Is 4.5 larger then 3.2?", 4.5 > 3.2)
# print("Is 4 smaller then 3?", 4 < 3)
# print("Is 4 smaller or equal to 3?", 4 <= 3)

# shopping_cart = ["apple", "milk"]
# shopping_cart2 = ["apple", "milk"]
# shopping_cart3 = ["milk", "apple"]
#
# print(shopping_cart == shopping_cart)
# print(shopping_cart is shopping_cart)
#
# print(shopping_cart == shopping_cart2)
# print(shopping_cart is shopping_cart2)
# # == porovnává jednotlivé položky v listu
# # is porovnává zda proměná ukazuje na stejné místo v paměti
# # is lze použít pouze objekty
#
# print(shopping_cart == shopping_cart3)  # is false because order of items matter
#
# print(4 != 3)
#
# evaluated = 4 != 3
# print(evaluated)
# print(type(evaluated))

# print("Can I drink?")
# legal_drinking_age = 18
# my_age = int(input("Enter your age: "))
#
# if my_age >= legal_drinking_age:
#     print("You can drink!")
#     print("Let's go party!")
# else:
#     print("just don't")
#
# print("after end")

#
# # print(bool(" ")) #don't use for now
#

# Else blok není povinný

# have_cat = False
# if have_cat:
#     print("pspsppsps - volám na kočku")
# # else:
# #     print("budu zticha- - nevolám na kočku")
#
# have_dog = False
# if have_dog:
#     print("haf haf - volám na psa")
# else:
#     print("budu zticha - nevolám na psa")
#
# else blok není povinný
# print("after end")
#
#
have_car = False
have_driving_license = False

print("ride?")

if not have_car:
    print("Get car first")
elif have_driving_license == False:
    print("Get driving license")
else:
    print("Let's go for a ride!")

# stejný zápis jako vejš ale bez elif - tady je horší čitelnost kvůli zanoření
if not have_car:
    print("Get car first")
else:
    if have_driving_license == False:
        print("Get driving license")
    else:
        print("Let's go for a ride!")


if have_car and have_driving_license:
    print("Let's go for a ride!")
else:
    print("You either don't have a car or license")

if have_car and have_driving_license:
    print("Let's go for a ride!")
else:
    if not have_car:
        print("Get car first")

    if not have_driving_license:
        print("Get license")

a = 40

if 40 < a < 65:
    print("Is in")

if a > 40 and a < 65:
    print("Is in")

# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# elif not have_car:
#     print("Get car first")
# elif not have_driving_license:
#     print("Get driving license")
#
#
# beer_in_fridge = True
# beer_in_basement = True
# beer_in_cupboard = True
#
# print("Do I have a beer at home?")
# if beer_in_fridge or beer_in_basement or beer_in_cupboard:
#     print("Yes I do!")
# else:
#     print("Let's go shopping!")
#
#
# ice_cream_found = True

# if ice_cream_found or spoon: #short circuit spoon is not checked because first part was true
#     print('let s have ice cream')
