# CACHE 101

Installation instruction for CACHE 

## Download REDIS
 
 Download  redis for -> [`link`](https://redis.io/download) 
 follow the installation instruction as mentioned in the page.
 
 To start redis server perform the following command in your terminal
 ```commandline
redis-server
```

## Create Virtual Environment
To run application in python3, just create a 
virtual environment

```
python3 -m venv .venv
```

Activate virtual environment by running the command

```
source .venv/bin/activate
```
___

## Install python dependencies
From the root of the project run:
```
make setup
```

## Running locally

```
make run
```
Now you can visit [`CACHE 1010`](http://127.0.0.1:5000) from your browser.

