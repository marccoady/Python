
import boto3

#How to upload 1 file

# s3_resource=boto3.client("s3")

#s3_resource.upload_file(
#    Filename="upload.png",
#    Bucket="mcoadyfirstbotobucket2",
# Key="uploadtest.png",
#    )
    
#How to upload multiple files

# import os
#import glob

# cwd=os.getcwd()

# cwd=cwd+"/upload"
#files=glob.glob("*.png")

#files

#for file in files:
    #s3_resource=boto3.client("s3")
    #s3_resource.upload_file(
    #Filename=file,
    #Bucket="mcoadyfirstbotobucket2",
    #Key=file.split("/")[-1])
    
    
# How to list S3 Ojbects

# s3_resource=boto3.client("s3")

# objects=s3_resource.list_objects(Bucket="mcoadyfirstbotobucket2")["Contents"]

# for object in objects:
#    print(object["Key"])

