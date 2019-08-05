import boto3
import sys, traceback
import time
from datetime import datetime
from time import sleep

def stop_ec2_instances():
    start_time = datetime.now()
    
    hora_atual = time.strftime('%H')

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
                    if instance['State']['Name'] == "running" and instance['Tags'] is not None : 
                        for tag in instance['Tags']:
                            try:
                                if (tag['Key'] == 'Stop' and tag['Value'] == '19:00' or tag['Value'] == '7:00pm') and hora_atual == "22"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop' and tag['Value'] == '20:00' or tag['Value'] == '8:00pm') and hora_atual == "23"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop' and tag['Value'] == '21:00' or tag['Value'] == '9:00pm') and hora_atual == "00"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop' and tag['Value'] == '22:00' or tag['Value'] == '10:00pm') and hora_atual == "01"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop' and tag['Value'] == '23:00' or tag['Value'] == '11:00pm') and hora_atual == "02"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop' and tag['Value'] == '00:00' or tag['Value'] == '0:00am') and hora_atual == "03"  :
                                    instanceIds.append(instance['InstanceId'])
                                if (tag['Key'] == 'Stop-Sab' and tag['Value'] == '15:00' or tag['Value'] == '3:00pm') and hora_atual == "18"  :
                                    instanceIds.append(instance['InstanceId'])
                            except:
                                print "Not expected error: ", traceback.print_exc()
                      
            if len(instanceIds) > 0 : 
                print "Stopping instances: " + str(instanceIds)
                ec2_client.stop_instances(InstanceIds=instanceIds, Force=False)                                                   
                                                            
        except:
            print "Not expected error:", traceback.print_exc()
                                                           
    end_time = datetime.now()
    took_time = end_time - start_time
    print "Total time of execution: " + str(took_time)    

def lambda_handler(event, context):
    print('Stopping instances... ')
    stop_ec2_instances()