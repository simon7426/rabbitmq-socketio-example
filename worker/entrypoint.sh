#!/bin/sh

echo "Waiting for rabbitmq..."

while ! nc -z rabbitmq 5672; do
    sleep 0.1
done

echo "Rabbitmq started"

exec "$@"