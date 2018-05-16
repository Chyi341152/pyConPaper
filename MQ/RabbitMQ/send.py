#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pika


# establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue to which the message will be delivered
channel.queue_declare(queue='hello')

# go through an exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Before exiting the program we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ.
# We can do it by gently closing the connection
connection.close()