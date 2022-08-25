# This program converts a set of numbers, assumed to be defined in Meters, to Kilometers.
# User inputted values are first written to a file to be saved and read back in to be processed.
numOfValues = int(input("How many values would you like to convert?: "))
file = open("text.txt", "w")

# collect the users inputs and store them in a file
for i in range(numOfValues):
    currentValue = input("Enter the a value: ")
    file.write(str(currentValue) + "\n")

file.close()
print("Values successfully written to file.\n")

# read and convert all values in the file from meters to kilometers
file = open("text.txt", "r")
for value in file:
    print(value.rstrip("\n"), "meters is equivalent to", (int(value) / 1000), "kilometers.")
file.close()