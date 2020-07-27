import tweepy 

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

print(key)
consumer_key = key[0]
consumer_secret =key[1]
access_token = key[2]
access_token_secret = key[3]
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
userid = api.get_user(screen_name = 'anthonydurrer')
print(userid.id)