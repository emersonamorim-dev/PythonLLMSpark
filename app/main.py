from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext

def main():
    spark = SparkSession.builder \
        .appName("LLMApplication") \
        .getOrCreate()

    ssc = StreamingContext(spark.sparkContext, 1)

    try:
        kafkaStream = KafkaUtils.createStream(
            ssc,
            'localhost:2181',  # Endereço do servidor Zookeeper
            'my_group',  # ID do grupo de consumidores
            {'my_topic': 1}  # Tópicos e número de threads
        )

        lines = kafkaStream.map(lambda x: x[1])

        lines.pprint()

        ssc.start()
        ssc.awaitTermination()

    except Exception as e:
        print("Erro ao processar os dados:", e)

if __name__ == "__main__":
    main()
