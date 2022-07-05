
import boto3

#upload 1 file

# s3_resource=boto3.client("s3")

#s3_resource.upload_file(
#    Filename="upload.png",
#    Bucket="mcoadyfirstbotobucket2",
# Key="uploadtest.png",
#    )
    
#upload multiple files

# import os
import glob

# cwd=os.getcwd()

# cwd=cwd+"/upload"
files=glob.glob("*.png")

files

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="mcoadyfirstbotobucket2",
    Key=file.split("/")[-1])
      
    