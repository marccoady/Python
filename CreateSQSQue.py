import boto3 #SDK needed to interact with AWS

sqs = boto3.resource('sqs') #SQS is the resource you need to manage the SQS feature 

    
queue = sqs.create_queue(QueueName='MyQue') #This will create your queue and name it
print(queue.url) #This will return your que URL