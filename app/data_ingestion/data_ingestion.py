from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext

def ingest_data(ssc):
    kafkaStream = KafkaUtils.createStream(
        ssc,
        'localhost:2181',  # Endereço do servidor Zookeeper
        'my_group',  # ID do grupo de consumidores
        {'my_topic': 1}  # Tópicos e número de threads
    )

    lines = kafkaStream.map(lambda x: x[1])

    return lines
