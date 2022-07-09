import boto3 #SDK needed to interact with AWS

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #the resource you will use to connect to your db

table = dynamodb.Table('pizza') #the table you will be scanning

response = table.scan() #This will scan the entire table
   
print(response) #This will print the response from the scan
