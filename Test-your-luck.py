# Defining a variable 'temperature'
temperature = 40
# Creating a decision structure to check the value of 'temperature'
if temperature < 15:
    # Printing a message if temperature is less than 15.
    print ("It's cold outside!")
elif temperature > 30:
    # Printing a message if temperature is greater than 30.
    print ("It's hot outside!")
else:
    # Printing a default message for other temperature values.
    print("The weather is moderate.")


level = 10

if level == 10:
    print ("you survived the night")
elif level < 10:
    input("1 or 2? ")