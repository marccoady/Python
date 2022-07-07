# how to create and launch instance using boto3

import boto3

ec2_resouce=boto3.resource('ec2')

ec2_resouce.create_instances(ImageId='ami-0cff7528ff583bf9a',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1)
