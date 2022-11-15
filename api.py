from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')




@storage.get('/')
def index():
    return"My name is Belise , this is my API"

@storage.get('/today')
def today():
    return str(datetime.now())

@storage.get('/myname')
def names(Fname: bool = False, last_name: bool = False):
    full_names = ""
    if Fname:
        full_names += 'Belise'
    if last_name:
        full_name += 'Gahongayire'
    return full_names
