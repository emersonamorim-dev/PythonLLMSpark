import logging

def store_data(df, mongodb_uri):
    try:
        # Escreva os dados transformados no MongoDB
        df.write.format("mongo").option("uri", mongodb_uri).mode("append").save()
        logging.info(f"Data successfully written to MongoDB at {mongodb_uri}")
    except Exception as e:
        logging.error(f"Failed to write data to MongoDB at {mongodb_uri}: {e}")
