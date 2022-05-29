from kafka import KafkaProducer
from json import dumps


producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   bootstrap_servers=['localhost:9092'])


producer.send("basic_topic",value="{'username': 'fbar', 'firstname': 'foo', 'lastname': 'bar'}", key="abc")