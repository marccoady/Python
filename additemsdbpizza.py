

import boto3 #SDK needed to interact with AWS



dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #the resource you will use to connect to your db

table = dynamodb.Table('pizza') #the table you will be updating

with table.batch_writer() as batch: #Items to add to your table
    batch.put_item(Item={"rank": 1, "name": "Delanceys"})
    batch.put_item(Item={"rank": 2, "name": "Serious Pie"})
    batch.put_item(Item={"rank": 3, "name": "Ballard Pizza Company"})
    batch.put_item(Item={"rank": 4, "name": "Camp Colvos"})
    batch.put_item(Item={"rank": 5, "name": "Bar Cotto"})
    batch.put_item(Item={"rank": 6, "name": "The Pizza Coop"})
    batch.put_item(Item={"rank": 7, "name": "Pagliacci"})
    batch.put_item(Item={"rank": 8, "name": "Zeeks"})
    batch.put_item(Item={"rank": 9, "name": "Costco"})
    batch.put_item(Item={"rank": 10, "name": "MOD"})
    
print(batch) #printing resutls to your screen