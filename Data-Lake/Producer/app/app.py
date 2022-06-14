from fileinput import filename
from kafka import KafkaProducer, TopicPartition
from fastapi import FastAPI, WebSocket
import json
from pydantic import BaseModel
from json import dumps
from ast import dump
import logging as log

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
   key_serializer=lambda x: json.dumps(x).encode("utf-8"),
   api_version =(0,10,1), 
   max_block_ms=5000
   )

    #overveje om der er for meget data tilgængelig eller for lidt.
class jsonObject(BaseModel):
     filename: str
     createddate: str
     data: bytes
     filetype: str
     version: str
     createdby: str

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/kafka/", response_model=jsonObject)
async def post(item: jsonObject):
    
    
    mytopic = "pdf_topic"
    producer.send(topic=mytopic, value=item).add_callback(on_send_success).add_errback(on_send_error)
    producer.flush(timeout=100)
    return jsonObject

    