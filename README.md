# CARD GAME API

## Pre-requisites

Python 3.7.9 installed

### DB for testing:

Another container running mongodb and set up with the below commands:

```bash

mongo admin -u root -p
MongoDB shell version v4.4.6
Enter password: 
db.createUser({user: "mongo_user", pwd: "mongo_password", roles: [ { role: "dbOwner", db: "mongo_db"}]})

```
### .env 

The file .env must be filled with the environment variables

## Start the container

+ docker-compose -p cardapi up with the mongo container up
To start it on a dev mode, you can use ```flask run -h 0.0.0.0 -p 8080```

## Structure of the API:

The main folder for the code is card_api. Inside, below the main folders:

+ apis: This folder contains the specifications file for the API in `specifications.yaml`. It also has the file 
+ common: This folder contanis the file where the exceptions are defined
+ config: Contains the config
+ core: This folder container the business logic. Inside there is 2 folders, applicaiton with the use cases and domain with the business entities
+ providers: this file contains the low level code with the repositories and a service to calculate the undealt cards