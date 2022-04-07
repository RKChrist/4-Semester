
import asyncio, websockets, json
import ssl, certifi
from kafka import KafkaProducer

""" Script that makes a connection to a websocket and sends 
each packet recieved to a topic on a Kafka server """

# mac'os needs this or it fails on SSL errors
# ssl_context = ssl.create_default_context()
# ssl_context.load_verify_locations(certifi.where())

# try and connect a local instance of Kafka
try:
    producer = KafkaProducer(
        bootstrap_servers=["broker:29092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
except Exception as ex:
    print("Exception while connecting Kafka")
    print(str(ex))


# listen to the websocket and publish the messages as a kafka data producer
async def listen(url, topic):
    # for mac; async with websockets.connect(url, ssl=ssl_context) as websocket:
    async with websockets.connect(url) as websocket:
        counter = 0
        while True:
            raw_packet = await websocket.recv()
            json_packet = json.loads(raw_packet)
            try:
                producer.send(topic, json.dumps(json_packet))
                producer.flush()
                print(
                    "Message " + str(counter) + " published successfully to Kafka topic"
                )
                counter = counter + 1
            except Exception as ex:
                print("Exception in publishing message")
                print(str(ex))
                return 0

if __name__ == "__main__":
    URL = "wss://<url of web socket>"
    topic = "test_topic"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(listen(URL, topic))