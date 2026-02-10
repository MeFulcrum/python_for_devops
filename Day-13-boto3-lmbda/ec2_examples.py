import boto3

def create_instance(image_id, instance_type='t2.micro', key_name=None, min_count=1, max_count=1):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(ImageId=image_id, InstanceType=instance_type, KeyName=key_name, MinCount=min_count, MaxCount=max_count)
    return [i.id for i in instances]

def list_instances(filters=None):
    ec2 = boto3.client('ec2')
    resp = ec2.describe_instances(Filters=filters or [])
    instances = []
    for r in resp.get('Reservations', []):
        for i in r.get('Instances', []):
            instances.append({'InstanceId': i['InstanceId'], 'State': i.get('State', {}).get('Name'), 'Tags': i.get('Tags', [])})
    return instances

def start_instances(instance_ids):
    ec2 = boto3.client('ec2')
    return ec2.start_instances(InstanceIds=instance_ids)

def stop_instances(instance_ids):
    ec2 = boto3.client('ec2')
    return ec2.stop_instances(InstanceIds=instance_ids)

def terminate_instances(instance_ids):
    ec2 = boto3.client('ec2')
    return ec2.terminate_instances(InstanceIds=instance_ids)

if __name__ == '__main__':
    print(list_instances())
