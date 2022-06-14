from kafka import KafkaConsumer, TopicPartition
from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import Optional
import datarefinement


app = FastAPI()

class jsonObject(BaseModel):
     filename: str
     createddate: str
     data: str
     filetype: str
     version: str
     createdby: str

class Item(BaseModel):
     message: Optional[list[str]] = []


@app.get('/kafka/', response_model=Item)
async def get_messages():
    item = Item()
    print("FUCK")
    result = []
    newresult = kafkaConsumer(result)  
    print("Woaws")
    for message in newresult:
        item.message.append(message.get('key').decode('utf-8') + ": username:" + message.get('username')+ ", " + "firstname:" + message.get('firstname') + ", lastname:" + message.get('lastname'))
        print("Type")
        print(type(item))
        print("Another one")

  
    return item

    
def kafkaConsumer(result):
    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(bootstrap_servers=['kafka-server1:9092'], 
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             sasl_mechanism="PLAIN",
                             auto_offset_reset='earliest'
                            )
    
    partitions = []
    for partition in consumer.partitions_for_topic('json_topic'):
        partitions.append(TopicPartition('json_topic', partition))
    
    end_offsets = consumer.end_offsets(partitions)
    endofstream = end_offsets.get(partitions[0])
    
    
    amount = endofstream
    print("amount")
    print(amount)
    if(amount <= 10):
        amount == 0
    else:
        amount = amount - 10
    

    par = TopicPartition(topic='json_topic', partition=0)
    consumer.assign([par])
    consumer.seek(par, amount) 
    count = 0
    for message in consumer: 
        result.append({"key": message.key,
                       "username":message.value.get('username'),
                       "firstname" : message.value.get('firstname'), 
                       "lastname" : message.value.get('lastname')})
        count = count + 1
        print(count)
        if(count==10):
            break
        
    print("works")
    return result