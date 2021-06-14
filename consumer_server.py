import asyncio

from confluent_kafka import Consumer

BROKER_URL = "PLAINTEXT://localhost:9093"

async def consume(topic_name):
    """Creates consumer and subscribes to topic"""
    consumer = Consumer({
        'bootstrap.servers': BROKER_URL,
        'group.id': '0'
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume()
        
        for message in messages:
            if message is None:
                print('Message is None')
            elif message.error() is not None:
                print('Error occurred: {}'.format(message.error()))
            else:
                print('{}\n'.format(message.value()))
                
        await asyncio.sleep(0.1)
                
def run_consumer():
    """Run consumer for some topic"""
    try:
        asyncio.run(consume('police.department.calls'))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
        
if __name__ == '__main__':
    run_consumer()