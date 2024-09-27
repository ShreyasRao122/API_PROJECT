import requests
response=requests.get("https://reqres.in/api/users")
data=response.json()
print(data)
with open("my_api_data.txt","a") as myfile:
    for i in data["data"]:
        print(i["first_name"] + " " + i["last_name"])
        myfile.write(i["first_name"] + " " + i["last_name"] + "\n")
