import json
from project.config import get_settings, Settings
import aio_pika

async def publish_message(message) -> None:
    settings: Settings = get_settings()
    connection = await aio_pika.connect(
        login=settings.rmq_user,
        password=settings.rmq_pass,
        host= settings.rmq_host
    )
    async with connection:
        routing_key = "test"
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=routing_key,
        )


async def declare_queue() -> None:
    settings: Settings = get_settings()
    connection = await aio_pika.connect(
        login=settings.rmq_user,
        password=settings.rmq_pass,
        host= settings.rmq_host
    )
    async with connection:
        channel = await connection.channel()
        await channel.declare_queue("test", durable=True)