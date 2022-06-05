from fileinput import filename
from kafka import KafkaProducer, TopicPartition
from fastapi import FastAPI, WebSocket
import json
from pydantic import BaseModel
from typing import Optional
import base64



app = FastAPI()

producer = KafkaProducer(
   value_serializer=lambda value: json.dumps(value).encode('utf-8'), 
   bootstrap_servers=['kafka-server1:9092'],
   retries=5,
   key_serializer=lambda x: json.dumps(x).encode("utf-8"),
   api_version =(0,10,1), 
   max_block_ms=5000
   )

class jsonObject(BaseModel):
     filename: str
     createddate: str
     data: bytes
     filetype: str
     version: str
     createdby: str



@app.post("/kafka", response_model=jsonObject)
async def post():
    
    
    
    producer.send()
    producer.flush(timeout=100)
    base64.b64encode()
    return jsonObject

    