import boto3
from botocore.exceptions import ClientError

def list_buckets():
    s3 = boto3.client('s3')
    resp = s3.list_buckets()
    return [b['Name'] for b in resp.get('Buckets', [])]

def upload_file(bucket, key, filename):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket, key)
    return True

def download_file(bucket, key, filename):
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, filename)
    return True

def object_exists(bucket, key):
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError:
        return False

if __name__ == '__main__':
    print(list_buckets())
    # Example usage:
    # upload_file('my-bucket', 'path/to/key.txt', 'local.txt')
    # download_file('my-bucket', 'path/to/key.txt', 'local-down.txt')
