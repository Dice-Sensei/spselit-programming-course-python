# while True:
#     filename = input("Zadej název souboru: ")

#     try:
#         my_file = open(filename, "rt")
#         print(my_file.read())
#         my_file.close()
#         break
#     except FileNotFoundError:
#         print(f"Soubor {filename} neexistuje")

# with open("cat.txt") as my_file:
#     print(my_file.read())

import json

with open("data.json") as json_file:

    json_loaded = json.load(json_file)

    print(json_loaded["members"]["4271633"])
