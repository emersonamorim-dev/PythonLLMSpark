# PythonLLMSpark
Codificação em Python para uma aplicação de Modelo de Linguagem de Grande Escala (LLM) que utiliza Apache Spark para processamento de dados, Apache Kafka para ingestão de dados em tempo real e MongoDB para armazenamento de dados. A aplicação é escrita em Python e utiliza o framework Tornado para a API.


## Requisitos

- Python 3.8+
- Apache Spark
- Apache Kafka
- MongoDB
- Docker (opcional)

## Instalação

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Inicie o servidor Kafka e crie um tópico chamado `my_topic`.
4. Inicie o servidor MongoDB.
5. Execute o script principal com `python main.py`.

## Testes

Os testes podem ser executados com `python -m unittest discover tests`.

## Docker

Um `Dockerfile` e um `docker-compose.yml` estão incluídos para a implantação com Docker. Para construir a imagem Docker, execute `docker build -t my_app .`. Para iniciar a aplicação com Docker Compose, execute `docker-compose up`.


## Autor
Emerson Amorim



