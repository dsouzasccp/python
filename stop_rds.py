import boto3
import time

def stop_rds_instances():
    
    hora_atual = time.strftime('%H')

    client = boto3.client('rds')
    response = client.describe_db_instances()
     
    for db in response['DBInstances']:
        db_instance_arn = db['DBInstanceArn']
     
     
        response = client.list_tags_for_resource(ResourceName=db_instance_arn)
        
        for tags in response['TagList']:
            if tags['Key'] == 'Stop' and tags['Value'] is not None :
                status = db['DBInstanceStatus']
                InstanceID = db['DBInstanceIdentifier']
                if status == 'available' :
                    if (tags['Key'] == 'Stop' and tags['Value'] == '20:00' or tags['Value'] == '8:00pm') and hora_atual == '23' :
                        print("shutting down %s " % InstanceID)
                        client.stop_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Stop' and tags['Value'] == '21:00' or tags['Value'] == '9:00pm') and hora_atual == '00' :
                        print("shutting down %s " % InstanceID)
                        client.stop_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Stop' and tags['Value'] == '22:00' or tags['Value'] == '10:00pm') and hora_atual == '01' :
                        print("shutting down %s " % InstanceID)
                        client.stop_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Stop' and tags['Value'] == '23:00' or tags['Value'] == '11:00pm') and hora_atual == '02' :
                        print("shutting down %s " % InstanceID)
                        client.stop_db_instance(DBInstanceIdentifier = InstanceID)
                    if (tags['Key'] == 'Stop' and tags['Value'] == '00:00' or tags['Value'] == '12:00am') and hora_atual == '03' :
                        print("shutting down %s " % InstanceID)
                        client.stop_db_instance(DBInstanceIdentifier = InstanceID)
                else:
                    print("The database " + InstanceID + " is " + status + " status!")
               
                    
                    

def lambda_handler(event, context):
    print('Stopping instances RDS... ')
    stop_rds_instances()