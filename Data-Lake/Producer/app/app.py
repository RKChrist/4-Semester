from fileinput import filename
from random import randint
from kafka import KafkaProducer, TopicPartition
from fastapi import FastAPI, WebSocket
import json
from pydantic import BaseModel
from ast import dump
import logging as log
from pathlib import Path
import base64
from typing import Optional
import random
import string

app = FastAPI()

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)
    print("Sent")


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    print("Ikke Sent")



producer = KafkaProducer(
   value_serializer=lambda value: json.dumps(value).encode('utf-8'), 
   bootstrap_servers=['kafka-server1:9092'],
   retries=5,
   key_serializer=lambda x: json.dumps(x).encode("utf-8"), max_request_size=101626282, buffer_memory=101626282
   )

    #overveje om der er for meget data tilgængelig eller for lidt.
     
     
class jsonObjectOut(BaseModel):
     filename: str
     createddate: str
     data: Optional[bytes]
     filetype: str
     version: int
     createdby: str





@app.post("/kafka/", response_model=jsonObjectOut)
async def post(item: jsonObjectOut):
    
    base_path = Path(__file__).parent
    files_path = (base_path / "Percy Jackson & the Olympians 01 - The Lightning Thief.pdf").resolve()
    data = open(files_path, 'rb')
    mytopic = "json_topic"
    jsonstring = [{"filename": item.filename, 
             "createddate": item.createddate, 
             "data": (data.read()).decode("latin-1"), 
             "filetype": item.filetype,
             "version" : item.version,
             "createdby":item.createdby}]
    
    producer.send(topic=mytopic, value=jsonstring[0], key=''.join(random.choice(string.ascii_letters) for i in range(20))).add_callback(on_send_success).add_errback(on_send_error)
    producer.flush(timeout=100)
    
    return item

#cqlsh -e "CREATE KEYSPACE connect WITH replication = {'class': 'NetworkTopologyStrategy','DC1': 1};"
#cqlsh -e "CREATE TABLE connect.pdf_table (userid text PRIMARY KEY, filename text, createddate date, data text, filetype text,version int, createdby text);"
#curl -X POST -H "Content-Type:application/json" -d "@/etc/kafka-connect/connectors/conf/json-connect.json" "http://localhost:8083/connectors"