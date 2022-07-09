#how to create an AWS ebs volume from snapshot using boto3 and python

import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1b',
        Encrypted=True,
        Size=8,
        SnapshotId='snap-0f23b4c70f064104c',
        VolumeType='gp2')
    



