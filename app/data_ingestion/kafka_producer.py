from kafka import KafkaProducer
import json

def send_message_to_kafka(topic, message):
    # Crie um produtor Kafka
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Envie a mensagem para o tópico especificado
    producer.send(topic, message)

    # Garanta que todas as mensagens foram enviadas
    producer.flush()
    producer.close()
