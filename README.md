



docker network create llm_twin

poetry self add 'poethepoet[poetry_plugin]'


from pymongo import MongoClient
client = MongoClient('mongodb://llm_engineering:llm_engineering@localhost:27017')
client = MongoClient('mongodb://llm_engineering:llm_engineering@mongo:27017')
client.server_info()


poetry poe test-poe