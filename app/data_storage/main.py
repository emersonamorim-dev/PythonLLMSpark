from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from spark_processing import process_data
from mongodb_storage import store_data

def main():
    spark = SparkSession.builder \
        .appName("LLMApplication") \
        .getOrCreate()

    ssc = StreamingContext(spark.sparkContext, 1)

    try:
        df = process_data(ssc)

        df.show()

        # Armazena os dados no MongoDB
        mongodb_uri = "mongodb://localhost:27017/PythonLLMSpark"
        store_data(df, mongodb_uri)

        # Inicie o processamento de streaming
        ssc.start()
        ssc.awaitTermination()

    except Exception as e:
        print("Erro ao processar os dados:", e)

if __name__ == "__main__":
    main()
