# Describe EBS volumes in AWS

import boto3
ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=[
            'snap-0f23b4c70f064104c'
            ])
            
x=ec2_boto3.describe_snapshots(SnapshotIds=[
            'snap-0f23b4c70f064104c'
            ])
            
print(x)
