import boto3

def create_user(user_name):
    iam = boto3.client('iam')
    return iam.create_user(UserName=user_name)

def attach_policy(user_name, policy_arn):
    iam = boto3.client('iam')
    return iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)

def detach_policy(user_name, policy_arn):
    iam = boto3.client('iam')
    return iam.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)

def delete_user(user_name):
    iam = boto3.client('iam')
    attached = iam.list_attached_user_policies(UserName=user_name).get('AttachedPolicies', [])
    for p in attached:
        iam.detach_user_policy(UserName=user_name, PolicyArn=p['PolicyArn'])
    return iam.delete_user(UserName=user_name)

if __name__ == '__main__':
    print(create_user('example-devops-user'))
