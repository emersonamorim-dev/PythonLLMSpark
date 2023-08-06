import logging

def store_data(df, mongodb_uri):
    try:
        # Escreve dados transformados no MongoDB
        df.write.format("mongo").option("uri", mongodb_uri).mode("append").save()
        logging.info(f"Dados gravados com sucesso no MongoDB em {mongodb_uri}")
    except Exception as e:
        logging.error(f"Falha ao gravar dados no MongoDB em {mongodb_uri}: {e}")
