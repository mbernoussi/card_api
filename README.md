# CARD GAME API

## Pre-requisites

Python 3.7.9 installed

### .env 

The file .env must be filled with the environment variables

## Start the services:

`./start.sh`
This scripts will prompt for two values, the mongo root password to initiate mongo and the mongo database password that will be used by the mongo user to store/retrieve the API data. This script will use the docker-compose file to build and run the API container and the mongo container.

## Structure of the API:

The main folder for the code is card_api. Inside, below the main folders:

+ apis: This folder contains the specifications file for the API in `specifications.yaml`. It also has the file 
+ common: This folder contanis the file where the exceptions are defined
+ config: Contains the config
+ core: This folder container the business logic. Inside there is 2 folders, applicaiton with the use cases and domain with the business entities
+ providers: this file contains the low level code with the repositories and a service to calculate the undealt cards