#utkarsh yadav
#2016kucp1023
#Code challenge 23
#to fetch the data from twitter
import json     #importing libraries.
import urllib2
import oauth2
import time
url1 = "https://api.twitter.com/1.1/search/tweets.json"#url for searching 
#initialising params dictionary.
params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="6qwAY8pkkNE0sgU7Ht1WpK4Ut", secret="wzW0DOIfku6Sha3maEfwY34aQDF7A3OHEgSZLE4phoOS01fzWW")#providing keys and secret from twitter application.
token = oauth2.Token(key="907490103035138048-r1D9ATeoDf9aKVIArgJmjAEWTUtEzKX", secret="aZ4lu2scMhR0cikoI256E3iB4VBnywMOYwtXpWoeHSJE6")#providing Tokens and secret from twitter application.
params["oauth_consumer_key"] = consumer.key #Variable autentication parameters.
params["oauth_token"] = token.key
print "Welocome to Twitter,You can search anything here\n"
ip=raw_input("Enter What you want to search : ")#taking topic from user
params["q"]=ip       

req = oauth2.Request(method="GET", url=url1, parameters=params)#Using get method to obtain json format information.
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token) #Requesting to sign in using tokens and keys.
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))#Storing the response in response object.

filename = params["q"]     
f = open(filename + "_File.txt", "w") #Writing to a file .
json.dump(data["statuses"], f)
f.close()
print "\nplease see the file for the content on the related topic  json format."

