
#!/usr/bin/env python3.7

my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

# We have used the str() method to convert the variable from an integer to a string. In most cases python will determine the type of data without having to declare it. However, it can be useful to tell python exactly how you want to treat the data type. Other examples are:

str() returns a string object
int() returns an integer object
float() returns a floating point object
bool() a boolean value of True or False