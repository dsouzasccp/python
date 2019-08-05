import boto3
import time

def start_rds_instances():
    
    hora_atual = time.strftime('%H')

    client = boto3.client('rds')
    response = client.describe_db_instances()
     
    for db in response['DBInstances']:
        db_instance_arn = db['DBInstanceArn']
     
     
        response = client.list_tags_for_resource(ResourceName=db_instance_arn)
        
        for tags in response['TagList']:
            if tags['Key'] == 'Start' and tags['Value'] is not None :
                status = db['DBInstanceStatus']
                InstanceID = db['DBInstanceIdentifier']
                if status == 'stopped' :
                    if (tags['Key'] == 'Start' and tags['Value'] == '07:45' or tags['Value'] == '7:45') and hora_atual == '10' :
                        print("starting up %s " % InstanceID)
                        client.start_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Start' and tags['Value'] == '08:00' or tags['Value'] == '8:00') and hora_atual == '11' :
                        print("starting up %s " % InstanceID)
                        client.start_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Start' and tags['Value'] == '09:00' or tags['Value'] == '9:00') and hora_atual == '12' :
                        print("starting up %s " % InstanceID)
                        client.start_db_instance(DBInstanceIdentifier = InstanceID)
                else:
                    print("The database " + InstanceID + " is " + status + " status!")
               
                    
                    

def lambda_handler(event, context):
    print('Starting instances RDS... ')
    start_rds_instances()