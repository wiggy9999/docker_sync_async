import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')
channel.basic_publish(exchange='', routing_key='test_queue', body='Hallo, Welt!')
print("Nachricht gesendet")
connection.close()
