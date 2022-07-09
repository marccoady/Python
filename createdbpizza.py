import boto3 #SDK needed to interact with 



dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #the resource you will use to create your db

table = dynamodb.create_table(
    TableName='pizza', #the name of table you are creating
    KeySchema=[
        {
            'AttributeName': 'rank',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[ #Attributes for the table
        {
            'AttributeName': 'rank',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10, #How many reads and writes configured per second
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status) #This will print the results of your script