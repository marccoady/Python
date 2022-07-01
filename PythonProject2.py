#!/usr/bin/env python3.7

# This Script can be used to create Random EC2 Names

# Import modules to generate random strings

import random
import string

# Verify department has access

while True:
    DeptName = input("Enter your Department: ")
    Department = ['Accounting', 'accounting', 'Marketing', 'marketing', 'FinOps', 'finops']
    if DeptName not in Department:
        print("Not Authorized to use this tool!")
        exit()
    else:
        break 
    
ec2_ammount = input("How many random EC2 names do you want generated? ")