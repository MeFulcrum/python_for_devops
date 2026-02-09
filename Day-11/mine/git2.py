import requests

repoName = "https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls"
response = requests.get(repoName)
data = response.json()

print("Type of data returned by the API:", type(data))

print("Keys of the dictionary:", data[0].keys())
print("Value of id field:", data[0]["id"])

print("Value of user login:", data[2]["user"]["login"])

for dt in range(len(data)):
    #print(f"user login of {dt} is : {data[dt]["user"]}")  #WROGN GIVES SYNTAX ERROR
    print(f"user login of {dt} is : {data[dt]['user']['login']} ")

# #List down all the user logins in the pull request data
# for dt in data:
#     print(f"user login is : {dt['user']['login']}")

#List down all user logins using for and range(len(data))
# for dt in range(len(data)):
#     print(f"user login is : {data[dt]['user']['login']}")


for dt in data:
    print(dt["user"]["login"])

for dt in range(len(data)):
    print(f" data of {dt} is : {data[dt]['user']['login']} ")