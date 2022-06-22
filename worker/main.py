import asyncio
import requests
import json
import os

import aio_pika

count = 0

async def update_user(user):
    url = f"http://winner:5000/api/v1/winner/update/{user}"
    requests.get(url)

async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        global count
        count += 1
        if count == 2:
            body = json.loads(message.body.decode('utf-8'))
            count = 0
            print(body)
            await update_user(body["user"])
            await asyncio.sleep(1)

async def main() -> None:
    print("Started listening on Rabbitmq")
    user = os.getenv("RABBIT_USER", "test")
    password = os.getenv("RABBIT_PASS", "test")
    host = os.getenv("RABBIT_HOST", "localhost")
    # logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust(
        f"amqp://{user}:{password}@{host}/",
    )

    queue_name = "test"
    print(f"Started listening on Rabbitmq at {host} with user {user}")

    async with connection:
        # Creating channel
        channel = await connection.channel()

        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=10)

        # Declaring queue
        queue = await channel.declare_queue(queue_name, durable=True)

        await queue.consume(process_message)
        try:
            await asyncio.Future()
        finally:
            connection.close()


if __name__ == "__main__":
    print("starting main print")
    asyncio.run(main())