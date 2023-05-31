# 1 Simple Message: Assign a message to a variable and then print that message.
message = 'Hello'
print(message)

# 2 Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
new_message = "I am learning Python"
print(new_message)
new_message = "I am improving my Python knowledge"
print(new_message)

# 3 Personal Message: Use a variable to represent a person's name and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like yo learn some Python today?"
name = "Alex"
print("Hello " + name + ", would you like to learn some Python today?")

# 4 Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.

name = "aLeX"
print(name.lower())
print(name.upper())
print(name.title())

# 5 Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look like the following, including the quotation marks: 
# Albert Einstein once said, "A person who never made a mistake in his life never tried anything new."
# Define the variables
quote = "You miss 100% of the shots you don't take -Wayne Gretzky"
author = "Michael Scott"

# Print the quote and author
print(author + " once said, \"" + quote + "\"")

# 6 Famous Quote 2: Repeat Exercise 5, but this time, represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
# Define the variables
famous_person = "Michael Gary Scott"
quote = "You miss 100% of the shots you don't take. - Wayne Gretzky"
message = famous_person + " once said, \"" + quote + "\""

# Print the message
print(message)

# 7 Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once
name = "      Alexander    "
name.strip()
name = name.strip()
print(name)
print("\t",name)
print("\n", name)