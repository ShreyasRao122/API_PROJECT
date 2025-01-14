import requests

class ApiData:
    def fetch_data(self):
        response = requests.get(self.url)
        self.data=response.json()
    def __init__(self,url):
        self.url=url
        self.data=[]

    def create_file(self,fname,mode):
        with open(fname, mode) as myfile:
            for i in self.data["data"]:
                myfile.write(i["first_name"] + " " + i["last_name"] + "\n")


a1=ApiData("https://reqres.in/api/users")
a1.fetch_data()
a1.create_file("./File2","a")



