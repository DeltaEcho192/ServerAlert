# Server Alert

### Description
A dockerized micro service which runs on python and peridoically makes http requests to check if given url's or local ip's return a 200 status code. If the given url or service is down a tweet is sent and users are alerted of the down server. This is to reduce response time to downed servers.


### Versions
#### Cloud Hosting:
    A docker container is run on a cloud hosting platform such a GCP or AWS.
        - Pros:
            * High alailability
        - Cons:
            * No local networks
            * Costs included
#### Localhosting:
    A docker container is run on a local sever, such as a raspberry pi.
        - Pros:
            * Local addresses can be called.
        - Cons:
            * If local power or internet go down the system wont be able to report.

#### Combination:
A combination could be used. A cloud server could make sure the local IP is active and a local server can ensure the uptime of the local network.
This way even if the local system fails the cloud server will report the whole system as down.

### Requirements:
    - Python
    - Twitter API Key
    - Docker

### Installation

* Create a Twitter developer account and get API keys and tokens
* Create a text file called keys.txt and enter your keys and username you want to DM in this order:
Consumer Key
Consumer Secret Key
Access Token
Access Secret Token
Username
* Then enter atleast 10 urls in registry.txt and increase urls by 10
* CD into directory
* Execute `docker-compose build`
* Execute `docker-compose up`
The system should be online and every 5 min check the status

DeltaEcho192