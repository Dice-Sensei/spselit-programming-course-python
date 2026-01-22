# Sometimes it is good to use not equal instead of negating equal
# print("Is 3 not equal to 4?", 3 != 4)
# print("Is 3 not equal to 4?", not (3 == 4))
# 3 != 4 # používanější varianta

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
# have_car = False
# have_driving_license = False
#
# print("ride?")
#
# if not have_car:
#     print("Get car first")
# elif have_driving_license == False:
#     print("Get driving license")
# else:
#     print("Let's go for a ride!")
#
# # stejný zápis jako vejš ale bez elif - tady je horší čitelnost kvůli zanoření
# if not have_car:
#     print("Get car first")
# else:
#     if have_driving_license == False:
#         print("Get driving license")
#     else:
#         print("Let's go for a ride!")
#
#
# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# else:
#     print("You either don't have a car or license")
#
# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# else:
#     if not have_car:
#         print("Get car first")
#
#     if not have_driving_license:
#         print("Get license")
#
# a = 40
#
# if 40 < a < 65:
#     print("Is in")
#
# if a > 40 and a < 65:
#     print("Is in")

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
# ice_cream_found = False

# if ice_cream_found and spoon: #short circuit spoon is not checked because first part was True
#     print('let s have ice cream')
