import requests

BASE = "http://127.0.0.1:5000/"

# data =[{"likes":10000,"name":"Rath Yatra Vlog","views":20000}
#        ,{"likes":1000,"name":"Rest API","views":8000}
#        ,{"likes":200,"name":"My  new House","views":2000}
#        ,{"likes":50,"name":"My City","views":1000}]

# for i in range(len(data)):
#     response = requests.put(BASE+"video/"+str(i),data[i])
#     print(response.json())
# input()

response = requests.delete(BASE+"video/0")
print(response)

input()

response = requests.get(BASE+"video/2")
print(response.json())

input()
response = requests.patch(BASE + "video/2", {"likes":1000})
print(response.json())