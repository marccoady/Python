#!/usr/bin/env python3.7

# This Script can be used to create Random EC2 Names
# Import modules to generate random strings and numbers

import random
import string

# Verify department has access

while True:
    DeptName = input("Enter your Department: ")
    Department = ['Accounting', 'accounting', 'Marketing', 'marketing', 'FinOps', 'finops']
    if DeptName not in Department:
        print("Not authorized to use this tool!")
        exit()
    else:
        break 
    
# Ask for how many EC2 names needed
    
ec2s = input("How many random EC2 instance names do you want created? ")
ec2s = int(ec2s)
for _ in range(ec2s):
    
# Generate the EC2 Instance names using the inputed information and random modules
# Define the characters of the random output that will be generated

    def randomstring(length=2, uppercase=True, lowercase=True, numbers=True):
        character_set = ''
        
        if uppercase:
            character_set += string.ascii_uppercase
        if lowercase:
            character_set += string.ascii_lowercase
        if numbers:
            character_set += string.digits
        
        return ''.join(random.choice(character_set) for i in range(length))
    rs = randomstring(4)
    
#Putting it all together and printing the results

    print("EC2 Instance Name: ")
    print(DeptName,'_', rs)
