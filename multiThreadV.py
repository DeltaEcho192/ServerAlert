import tweepy 
import requests
import threading


def statusCheck(link):
    
    up = True
    try:
        response = requests.get(link)

        if response.status_code == 200:
            print('Success Website = ' + link)
    except:
        print("Status 404")
        up = False
        sendTweet(link)
    return up


def sendTweet(serverNames):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        
        auth.set_access_token(access_token, access_token_secret) 
        api = tweepy.API(auth) 
        
        userid = api.get_user(screen_name = 'anthonydurrer')
        print(userid.id)
        api.send_direct_message(userid.id,"A Server has gone Down. " + serverNames)
    except:
        print("There has been an error...")
    else:
        print("Connection and message succesfully sent")

if __name__ == "__main__": 
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
    i = 0
    x = 0
    
    while i < (len(links) / 4):
        t1 = threading.Thread(target=statusCheck, args=(links[x],)) 
        print(links[x])
        t2 = threading.Thread(target=statusCheck, args=(links[x+1],))
        print(links[x+1])
        t3 = threading.Thread(target=statusCheck, args=(links[x+2],)) 
        print(links[x+2])
        t4 = threading.Thread(target=statusCheck, args=(links[x+3],)) 
        print(links[x+3])
        t1.start() 
        t2.start() 
        t3.start() 
        t4.start() 
        t1.join() 
        t2.join()
        t3.join()
        t4.join()
        i = i + 1
        x = x + 4

    print("Done!") 
