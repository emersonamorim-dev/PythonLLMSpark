from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext

def process_data(ssc):
    kafkaStream = KafkaUtils.createStream(
        ssc,
        'localhost:2181',  # Endereço do servidor Zookeeper
        'my_group',  # ID do grupo de consumidores
        {'my_topic': 1}  # Tópicos e número de threads
    )

    lines = kafkaStream.map(lambda x: x[1])

    transformed_lines = lines.map(lambda line: line.upper())

    # Converte o DStream em um DataFrame
    df = transformed_lines.toDF()

    df.write.format("mongo").mode("overwrite").save()

    return df
