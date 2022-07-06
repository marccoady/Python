#how to create VPC

# import boto3

# client=boto3.client("ec2")

# client.create_vpc(CidrBlock='10.0.0.0/16')

# Describe a VPC

import boto3

client=boto3.client("ec2")

#how to describe all vpcs available in your account

x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

# No of VPCs in your AWS

len(no_of_vpcs)

# Printing the ids of your VPCs

for vpc in no_of_vpcs:
    print(vpc["VpcId"])

# print(response)

# testing


# response=client.describe_vpcs()

# print(response)

