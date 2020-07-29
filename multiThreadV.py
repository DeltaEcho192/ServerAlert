import tweepy 
import requests
import threading
import time

start_time = time.time()


def statusCheck(link,username,cKey,cSKey,acToken,acSToken):
    
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print('Success Website = ' + link)
    except:
        print("Status 404")
        up = False
        sendTweet(link,username,cKey,cSKey,acToken,acSToken)

def sendTweet(serverNames,username,cKey,cSKey,acToken,acSToken):
    try:
        print(consumer_key)
        auth = tweepy.OAuthHandler(cKey, cSKey) 
        
        auth.set_access_token(acToken, acSToken) 
        api = tweepy.API(auth) 
        
        userid = api.get_user(screen_name = username)
        print(userid.id)
        api.send_direct_message(userid.id,"A Server has gone Down. " + serverNames)
        return "message Sent"
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
    username = key[4]

    f.close()

    f = open('registaryTest.txt',"r")

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
    t = 1
    print(int((len(links)/10)))
    testVar = "Hello world"
    while t == 1:
        print("Executing Check")
        i = 0
        x = 0
        while i < (int(len(links) / 10)):
            t1 = threading.Thread(target=statusCheck, args=(links[x],username,consumer_key,consumer_secret,access_token,access_token_secret)) 
            t2 = threading.Thread(target=statusCheck, args=(links[x+1],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t3 = threading.Thread(target=statusCheck, args=(links[x+2],username,consumer_key,consumer_secret,access_token,access_token_secret)) 
            t4 = threading.Thread(target=statusCheck, args=(links[x+3],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t5 = threading.Thread(target=statusCheck, args=(links[x+4],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t6 = threading.Thread(target=statusCheck, args=(links[x+5],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t7 = threading.Thread(target=statusCheck, args=(links[x+6],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t8 = threading.Thread(target=statusCheck, args=(links[x+7],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t9 = threading.Thread(target=statusCheck, args=(links[x+8],username,consumer_key,consumer_secret,access_token,access_token_secret))
            t10 = threading.Thread(target=statusCheck, args=(links[x+9],username,consumer_key,consumer_secret,access_token,access_token_secret))
            

            t1.start() 
            t2.start() 
            t3.start() 
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()
            
            t1.join() 
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            t8.join()
            t9.join()
            t10.join()


            i = i + 1
            x = x + 10
        time.sleep(300)
        

    print("Done!") 
    print("--- %s seconds ---" % (time.time() - start_time))
