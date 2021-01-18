import requests    #importing the request module ,json module,urllib2 module
import json
import urllib2
# defining the api-endpoint 
API_ENDPOINT = " http://35.154.116.182/api_v0.1/sending"
# data to be sent to api
data = {"Phone_Number":"9807534919",
        "Name":"Utkarsh_yadav",
        "College_Name":"IIITKOTA",
        "Branch":"CSE"
      }
#second data to be sent to api
data1 = {
        "Phone_Number":"9795945935",
        "Name":"Ayush Sharma",
        "College_Name":"IIITKOTA",
        "Branch":"CSE"
      }
r = requests.post(url = API_ENDPOINT, json = data)
r1 = requests.post(url = API_ENDPOINT, json = data1)

# extracting response text
t=r.json()
for i in t:
    print i,":",t[i]
t1=r1.json()
for i in t1:
    print i,":",t1[i]
post_data = "http://35.154.116.182/api_v0.1/receiving"

phone=raw_input("enter the phone number")#takeing number from user
PARAMS ={"Phone_Number":phone}
response=requests.get(url=post_data,params=PARAMS)
record=response.json()
for i in record:  #producing output
    print i,":",record[i]
