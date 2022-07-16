import json #Importing json module
import boto3 #Importing boto3 module
import random #Needed to create a random nubmer
import string #Importing string

def lambda_handler(event, context): #Event and context is required
    
    #Set your variables to define the function, to create messages with random numbers
    n = string.digits
    some_num = ( ''.join(random.choice(n) for i in range(40))) #This will create the random numbers
    m = "This is the a random number created by Python: "+str(some_num) #The message that will be sent plus random number
    

    
    client = boto3.client('sqs') #Client needed to interact with SQS
    
    #Puts things all together to send the message to the que 
    client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/412765341264/MyQue", 
        MessageBody=some_num)
        
    
    #What will be returned during testing, 
    return {
        'statusCode' : 200,
        'body' : json.dumps(m)
    }