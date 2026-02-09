import requests

repoName = "https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls"

response = requests.get(repoName) 

data = response.json()

print(response.status_code)

#Write down all the pull request titles in the repository
for i in data:
    print("titel is ", i['title'])
    break

#Write down all the pull request numbers in the repository
for i in data:
    print("number is ",i['number'])
    break

#Write down type of data returned by the API
print("Type of data returned by the API:", type(data))

#COnvert list to dictionary
data_dict = {i['number']: i['title'] for i in data}

#Chekc type of data_dict
print("Type of data_dict:", type(data_dict))

#Write down all the keys of dictionary
print("Keys of the dictionary:", data_dict.keys())

print("Values of the dictionary:", data_dict.values())
