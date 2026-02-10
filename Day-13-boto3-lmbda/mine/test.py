import boto3

client = boto3.client('s3')

try:
    response_create = client.create_bucket(
        Bucket='my-gaju-bucket-9',
    )
    print("Bucket created:", response_create.get('BucketArn',{}))
except Exception as e:
    print("Error creating bucket:", e)

# response_create = client.create_bucket(
#     Bucket='my-gaju-bucket-9',
# )

response_list = client.list_buckets()
print("Response from list_buckets:", response_list)  # Print the full response for debugging
print("Status :" , response_list['ResponseMetadata']['HTTPStatusCode'])  # Print the HTTP status code)
for i in range(len(response_list['Buckets'])):
    print("Buckets" , response_list['Buckets'][i]['Name'])

for i in response_list['Buckets']:
    print("Buckets via get" , i['CreationDate'])

for buk in response_list:
    print("Bucket Name:", buk)

#
# print("Bucket List" , response_list)

response_del = client.delete_bucket(
    Bucket='my-gaju-bucket-9',
)
print ("Bucket deletion response:", response_del)  # Print the full response for debugging

if response_del['ResponseMetadata']['HTTPStatusCode'] == 204:
    print("Bucket deleted successfully")

for bt in response_list:
    print("Buckets:", bt)
