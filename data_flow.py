is_true = True
is_false = False

print(4 > 3)

evaluated = 4 != 3
print(evaluated)

# print(bool(" ")) #don't use for now

legal_drinking_age = 18
my_age = 17

if my_age >= legal_drinking_age:
    print("You can drink!")
    print("Let's go party!")
else:
    print("just don't")

print("after end")

have_cat = False

if have_cat:
    print("pspsppsps")


have_car = True
have_driving_license = False

print("ride?")

if not have_car:
    print("Get car first")
elif have_driving_license == False:
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


if have_car and have_driving_license:
    print("Let's go for a ride!")
elif not have_car:
    print("Get car first")
elif not have_driving_license:
    print("Get driving license")


beer_in_fridge = True
beer_in_basement = True
beer_in_cupboard = True

print("Do I have a beer at home?")
if beer_in_fridge or beer_in_basement or beer_in_cupboard:
    print("Yes I do!")
else:
    print("Let's go shopping!")


ice_cream_found = True

# if ice_cream_found or spoon: #short circuit spoon is not checked because first part was true
#     print('let s have ice cream')
