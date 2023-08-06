import unittest
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from spark_processing import process_data

class TestSparkProcessing(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder \
            .appName("TestLLMApplication") \
            .getOrCreate()

        self.ssc = StreamingContext(self.spark.sparkContext, 1)

    def tearDown(self):
        self.ssc.stop()

    def test_process_data(self):
        # Crie um DStream de exemplo
        rdd = self.spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7])
        dstream = self.ssc.queueStream([rdd])

        # Chame a função process_data
        df = process_data(dstream)

        # Verifique se o DataFrame resultante tem o formato esperado
        self.assertEqual(df.columns, ['expected', 'column', 'names'])
        self.assertEqual(df.count(), 5)

if __name__ == '__main__':
    unittest.main()

