
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ecs')
    
    cluster = 'Clutser-xgboost-ecs-demo'
    task_name = 'ml-ecs-demo'
    subnets = ['subnet-572f8b2c']
    security_groups = ['sg-156d787a']
    
    
    response = client.run_task(
          cluster=cluster,
          taskDefinition=task_name,
          count=1,
          launchType='FARGATE',
          networkConfiguration={
              'awsvpcConfiguration': {
                  'subnets': subnets,
                  'securityGroups': security_groups,
                  'assignPublicIp': 'ENABLED'
              }
          }
    )
