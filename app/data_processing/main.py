from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from spark_processing import process_data

def main():
    spark = SparkSession.builder \
        .appName("LLMApplication") \
        .config("spark.mongodb.input.uri", "mongodb://localhost:27017/test.myCollection") \
        .getOrCreate()

    ssc = StreamingContext(spark.sparkContext, 1)

    try:
        df = process_data(ssc)
        df.show()

        # Inicia o processamento de streaming
        ssc.start()
        ssc.awaitTermination()

    except Exception as e:
        print("Erro ao processar os dados:", e)

if __name__ == "__main__":
    main()
