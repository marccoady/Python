import boto3

aws_resouce=boto3.resource("s3")
bucket=aws_resouce.Bucket("mcoadybotobucketagain2022")


response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
        
    },

)

print(response)