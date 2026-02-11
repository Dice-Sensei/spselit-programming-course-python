# Reading and writing files is often used to get inputs write outputs of a program without a need for user interaction
# Sometimes it is called IO operations (input/output)

# OS handles manipulation of files we are just using it

# Example basic reading
file_handle = open("cat.txt")  # file resource is provided
print("Handle information:", file_handle)
print("File content:", file_handle.read())
file_handle.close()  # we are responsible for closing the file


# Example basic reading using with keyword
# This way we don't have to close the file as with will doit for us
with open("cat.txt") as file_handle:
    print("Handle information:", file_handle)
    print("File content:", file_handle.read())

# Example reading file with a filepath provided by the user with proper error handling
filename = input("File to open: ")
try:
    with open(filename) as file_handle:
        print("File content:", file_handle.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")


# Function open() allows us to specify how to open a file (for example, for writing) or what codding use to properly handle it

# import json
#
# with open("data.json") as json_file:
#
#     json_loaded = json.load(json_file)
#
#     print(json_loaded["members"]["4271633"])
