import pika
def callback(ch, method, properties, body):
    print(f"Nachricht empfangen: {body}")
    ch.stop_consuming()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
print("Warte auf Nachricht...")
channel.start_consuming()
connection.close()
