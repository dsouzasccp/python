import boto3
import sys, traceback
import time
from datetime import datetime
from time import sleep

def start_ec2_instances():
    start_time = datetime.now()
    hora_atual = str(time.strftime('%H'))

    print('hora = ' + hora_atual)
    
    # starting ec2 client
    ec2_client = boto3.client('ec2')

    regions = ec2_client.describe_regions()

    for region in regions['Regions']:
        try:
            print("Region: " + str(region['RegionName']))
            ec2_client = boto3.client('ec2', region_name=region['RegionName'])
            instances = ec2_client.describe_instances()
            instanceIds = list()
            
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    if instance['State']['Name'] == "stopped" and instance['Tags'] is not None : 
                        for tag in instance['Tags']:
                            try:
                                if (tag['Key'] == 'Start' and tag['Value'] == '05:00' or tag['Value'] == '5:00') and hora_atual == '08'  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Start' and tag['Value'] == '06:00' or tag['Value'] == '6:00') and hora_atual == '09'  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Start' and tag['Value'] == '07:00' or tag['Value'] == '7:00') and hora_atual == '10'  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Start' and tag['Value'] == '08:00' or tag['Value'] == '8:00') and hora_atual == '11'  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Start' and tag['Value'] == '09:00' or tag['Value'] == '9:00') and hora_atual == '12'  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Start-Sab' and tag['Value'] == '08:30' or tag['Value'] == '8:30') and hora_atual == '11'  :
                                    instanceIds.append(instance['InstanceId'])
                            except:
                                print "Not expected error: ", traceback.print_exc()
                      
            if len(instanceIds) > 0 : 
                print "Starting instances: " + str(instanceIds)
                print(hora_atual)
                ec2_client.start_instances(InstanceIds=instanceIds)                                                   
                                                            
        except:
            print "Not expected error:", traceback.print_exc()
                                                           
    end_time = datetime.now()
    took_time = end_time - start_time
    print "Total time of execution: " + str(took_time)    

def lambda_handler(event, context):
    print('Starting instances... ')
    start_ec2_instances()