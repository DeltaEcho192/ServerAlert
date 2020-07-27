import tweepy 
import requests


key = []

f = open('keys.txt','r')

for x in f:
    key.append(x)

i = 0
while i < (len(key) - 1):
    work = key[i]
    work = work[:-1]
    key[i] = work
    i = i + 1

consumer_key = key[0]
consumer_secret =key[1]
access_token = key[2]
access_token_secret = key[3]

f.close()

f = open('registry.txt',"r")

links = []
for c in f:
    links.append(c)

v = 0
while v < (len(links) - 1):
    work = links[v]
    work = work[:-1]
    links[v] = work
    v = v + 1

print(links)

up = True

b = 0
while b < len(links):
    try:
        response = requests.get(links[b])

        if response.status_code == 200:
            print('Success!')
    except:
        print("Status 404")
        up = False


    if up == False:
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
            
            auth.set_access_token(access_token, access_token_secret) 
            api = tweepy.API(auth) 
            
            userid = api.get_user(screen_name = 'anthonydurrer')
            print(userid.id)
            api.send_direct_message(userid.id,"A Server has gone Down.")
        except:
            print("There has been an error...")
        else:
            print("Connection and message succesfully sent")
    b = b + 1
    up = True
