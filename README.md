

# Following 'LLM-engineer handbook'

docker network create llm_twin

poetry self add 'poethepoet[poetry_plugin]'


from pymongo import MongoClient
client = MongoClient('mongodb://llm_engineering:llm_engineering@localhost:27017')
client = MongoClient('mongodb://llm_engineering:llm_engineering@mongo:27017')
client.server_info()


poetry poe test-poe


1. Scraping web data 
2. Raw data documents in mongo db 
3. Preprocessing 
4. Chunking 
5. Embedding 
6. Embeddings into qdrant 
7. create SFT dataset, using openai