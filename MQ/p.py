import pika


con = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = con.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
print("[x] Sent 'Hello World!'")
con.close()

