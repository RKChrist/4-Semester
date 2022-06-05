from ast import dump
from email import message
from kafka import KafkaProducer
from json import dumps
import logging as log
import random
import string


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)
    print("Sent")


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    print("Ikke Sent")

producer = KafkaProducer(
   value_serializer=lambda value: dumps(value).encode('utf-8'), 
   bootstrap_servers=['kafka-server1:9092'],
   retries=5,
   key_serializer=lambda x: dumps(x).encode("utf-8"),
   api_version =(0,10,1), 
   max_block_ms=5000
   )
messages = [{"username": ''.join(random.choice(string.ascii_letters) for i in range(20)), 
             "firstname": ''.join(random.choice(string.ascii_letters) for i in range(20)), 
             "lastname": ''.join(random.choice(string.ascii_letters) for i in range(20))}]
letters = ''.join(random.choice(string.ascii_letters) for i in range(20))
print(messages)
print(letters)
value=letters

producer.send(topic="json_topic", value=messages[0], key=value).add_callback(on_send_success).add_errback(on_send_error)
producer.flush(timeout=100)

producer.close(timeout=500)


