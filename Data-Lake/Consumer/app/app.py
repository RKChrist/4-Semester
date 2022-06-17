from kafka import KafkaConsumer, TopicPartition
from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import Optional



app = FastAPI()

class jsonObjectOut(BaseModel):
     filename: str
     createddate: str
     data: Optional[bytes]
     filetype: str
     version: int
     createdby: str




# @app.get('/kafka/', response_model=Item)
# async def get_messages():
#     item = Item()
#     print("FUCK")
#     result = []
#     newresult = kafkaConsumer(result)  
#     print("Woaws")
#     for message in newresult:
#         item.message.append(message.get('key').decode('utf-8') + ": username:" + message.get('username')+ ", " + "firstname:" + message.get('firstname') + ", lastname:" + message.get('lastname'))
#         print("Type")
#         print(type(item))
#         print("Another one")

  
#     return item
@app.get('/kafka/')
async def get_messages():
    result = []
    newresult = kafkaConsumer(result)  
    return newresult
        

  
    return "Hello"

    
def kafkaConsumer(result):
    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(bootstrap_servers=['kafka-server1:9092'], 
                            #  value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             sasl_mechanism="PLAIN",
                             auto_offset_reset='earliest'
                            )


    par = TopicPartition(topic='json_topic', partition=2)
    consumer.assign([par])
    consumer.seek(par, 0) 
    
    for item in consumer: 
        val = item.value.decode('utf-8')
        result = val
        break
        # result.append({"filename": item.value.filename, 
        #      "createddate": item.value.createddate, 
        #      "data": item.value.data.decode("utf-8"), 
        #      "filetype": item.value.filetype,
        #      "version" : item.value.version,
        #      "createdby":item.value.createdby})
        # count = count + 1
        # print(count)
        
        
    print("works")
    return result