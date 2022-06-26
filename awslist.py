#!/usr/bin/env python3.7

# 1. Creating Empty List

awslist = []

# 2. Appending list of AWS Services

awslist.append('EC2')
awslist.append('S3')
awslist.append('DyanamoDb')
awslist.append('Vpc')
awslist.append('Lambda')

# 3. Print the list and length

print(awslist)
print("Original Length : ", len(awslist))

#4. Delete 2 services from the list

del awslist[0:2]

#5. Printing modified list and length

print(awslist)
print("Modified Length : ", len(awslist))





